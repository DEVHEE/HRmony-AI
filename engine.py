"""
HRmony AI - Multi-Agent Simulation Engine and Mathematical Formulations
Calibrated to Proposal Specification [표 4] and [설계 모듈 1~4]
"""

import numpy as np
import pandas as pd

FIRST_NAMES = ["김", "이", "박", "최", "정", "강", "조", "윤", "장", "임", 
               "한", "오", "서", "신", "권", "황", "안", "송", "전", "홍"]
GIVEN_NAMES = ["도윤", "서진", "하은", "민호", "지훈", "준영", "동훈", "지우", 
               "예은", "시우", "유진", "수아", "현우", "지아", "태윤", "채원", 
               "건우", "윤아", "도현", "서아", "승우", "다은", "연우", "민서"]

def generate_agent_population(n=500, seed=42):
    """Generates initial population of N employee agents with baseline attributes."""
    rng = np.random.default_rng(seed)
    
    agents = []
    for i in range(1, n + 1):
        emp_id = f"EMP-{i:03d}"
        f_name = rng.choice(FIRST_NAMES)
        g_name = rng.choice(GIVEN_NAMES)
        name = f"{f_name}{g_name}"
        
        # Tenure: 1 to 15 years
        # Slight skew towards junior-mid
        tenure = int(rng.choice(range(1, 16), p=[
            0.14, 0.13, 0.12, 0.10, 0.09, 0.08, 0.07, 0.06,
            0.05, 0.04, 0.03, 0.03, 0.02, 0.02, 0.02
        ]))
        
        # Unified Level mapping
        if tenure <= 4:
            level = "L4"
            level_name = "선임 (Junior)"
        elif tenure <= 8:
            level = "L5"
            level_name = "책임 / 파트장 (Senior)"
        elif tenure <= 11:
            level = "L6"
            level_name = "수석 / 팀장 (Staff)"
        elif tenure <= 14:
            level = "L7"
            level_name = "전문위원 / 실장 (Principal)"
        else:
            level = "L8"
            level_name = "펠로우 / 본부장 (Fellow)"
            
        # Behavior logs & propensity
        ic_prop = float(np.clip(rng.beta(2.2, 2.0), 0.10, 0.95))
        mgr_prop = float(np.clip(rng.beta(2.0, 2.2), 0.10, 0.95))
        
        # Initial Skill index
        initial_skill = float(np.clip(rng.normal(86, 7), 68, 100))
        
        # Special Presets for specific case studies in Proposal
        if i == 42:
            name = "김도윤"
            tenure = 9
            level = "L6"
            level_name = "수석 / 팀장 (Staff)"
            ic_prop = 0.91
            mgr_prop = 0.24
            initial_skill = 94.0
        elif i == 108:
            name = "이서진"
            tenure = 7
            level = "L5"
            level_name = "책임 / 파트장 (Senior)"
            ic_prop = 0.89
            mgr_prop = 0.28
            initial_skill = 95.5
        elif i == 215:
            name = "박지훈"
            tenure = 6
            level = "L5"
            level_name = "책임 / 파트장 (Senior)"
            ic_prop = 0.32
            mgr_prop = 0.86
            initial_skill = 81.0
            
        agents.append({
            "emp_id": emp_id,
            "name": name,
            "tenure": tenure,
            "level": level,
            "level_name": level_name,
            "ic_propensity": ic_prop,
            "mgr_propensity": mgr_prop,
            "initial_skill": initial_skill
        })
        
    return pd.DataFrame(agents)

def run_simulation(n_agents=500, months=60, seed=42, decay_rate=0.25, 
                   salary_pressure="보통", control_forced_mgr_rate=0.65, 
                   reskill_efficiency=0.85, royalty_rate=0.04, 
                   mgr_bonus_weight=0.035, veto_enabled=True, l6_cutoff=3.5):
    """
    Executes the multi-agent organizational simulation over t=1..months.
    Calibrated strictly to Table 4 benchmark targets at seed=42 default inputs.
    """
    df_pop = generate_agent_population(n_agents, seed)
    
    # Calibration coefficients
    decay_ratio = decay_rate / 0.25
    eff_ratio = reskill_efficiency / 0.85
    forced_ratio = control_forced_mgr_rate / 0.65
    royalty_ratio = royalty_rate / 0.04
    l6_ratio = l6_cutoff / 3.5
    
    press_map = {"낮음": 0.90, "보통": 1.00, "높음": 1.15}
    press_factor = press_map.get(salary_pressure, 1.0)
    
    # 6 Key Targets Calibration at t=months
    # 1) High IC Attrition (Ctrl 38.4% vs Treat 11.2%)
    target_ic_attr_ctrl = 38.4 * (0.8 + 0.2 * forced_ratio) * (0.9 + 0.1 * decay_ratio) * press_factor
    target_ic_attr_treat = 11.2 * (1.2 - 0.2 * eff_ratio) * (1.05 if not veto_enabled else 1.0) * press_factor
    
    # 2) Domino Attrition (Ctrl 29.6% vs Treat 6.8%)
    target_domino_ctrl = 29.6 * forced_ratio
    target_domino_treat = 6.8 * (1.1 - 0.1 * eff_ratio)
    
    # 3) Tech Skill Fulfillment (Ctrl 46.5% vs Treat 88.4%)
    target_tech_ctrl = 46.5 / (0.8 + 0.2 * decay_ratio)
    target_tech_treat = 88.4 * eff_ratio / (0.9 + 0.1 * decay_ratio)
    
    # 4) Recovery Duration (Ctrl 5.8 mo vs Treat 1.4 mo)
    target_rec_ctrl = 5.8 * (0.9 + 0.1 * decay_ratio)
    target_rec_treat = 1.4 * (1.0 / (royalty_ratio ** 0.25))
    
    # 5) Annual Defect / Rework Loss Defense (Ctrl -8.2 억 vs Treat +31.5 억)
    target_rework_loss_ctrl = -8.2 * (0.85 + 0.15 * forced_ratio)
    veto_mult = 1.0 if veto_enabled else 0.40
    target_rework_defense_treat = 31.5 * veto_mult * (l6_ratio ** 0.15)
    
    # 6) HCROI (Ctrl 1.32x vs Treat 2.84x)
    target_hcroi_ctrl = 1.32 / (0.9 + 0.1 * decay_ratio)
    target_hcroi_treat = 2.84 * (0.7 + 0.3 * eff_ratio) * (0.9 + 0.1 * royalty_ratio)
    
    # Build Monthly Trajectories (t=1..months)
    t = np.arange(1, months + 1)
    progress = t / months
    
    # Sigmoidal growth curves for attrition
    s_curve = 1.0 / (1.0 + np.exp(-6 * (progress - 0.45)))
    s_norm = (s_curve - s_curve[0]) / (s_curve[-1] - s_curve[0])
    
    # IC Attrition Time series
    ic_attr_ctrl_series = target_ic_attr_ctrl * s_norm
    ic_attr_treat_series = target_ic_attr_treat * s_norm
    
    # Domino Attrition Time series
    domino_ctrl_series = target_domino_ctrl * s_norm
    domino_treat_treat_series = target_domino_treat * s_norm
    
    # Skill fulfillment decay and recovery
    # Control continuously decays from ~92% down to target
    skill_decay_curve = 92.0 - (92.0 - target_tech_ctrl) * (1 - np.exp(-2.2 * progress))
    # Treatment dips slightly then recovers and stays high
    skill_treat_curve = 92.0 - 6.0 * np.sin(np.pi * progress) * (1 - eff_ratio * 0.5)
    skill_treat_curve = np.clip(skill_treat_curve * (target_tech_treat / 88.4), 60.0, 96.0)
    
    # Reskilled count
    reskilled_treat = (n_agents * 0.78 * eff_ratio * progress).astype(int)
    reskilled_ctrl = (n_agents * 0.12 * progress).astype(int)
    
    # Cumulative Rework Loss / Defense (in 억원)
    cum_rework_loss_ctrl = target_rework_loss_ctrl * (t / 12.0)
    cum_rework_defense_treat = target_rework_defense_treat * (t / 12.0)
    
    # HCROI trajectory
    hcroi_ctrl_series = 1.25 + (target_hcroi_ctrl - 1.25) * progress
    hcroi_treat_series = 1.40 + (target_hcroi_treat - 1.40) * (progress ** 0.8)
    
    # Net Financial Contribution cumulative
    net_fin_ctrl = 184.2 * (t / 60.0) * (target_hcroi_ctrl / 1.32)
    net_fin_treat = 425.6 * (t / 60.0) * (target_hcroi_treat / 2.84)
    
    timeseries_df = pd.DataFrame({
        "month": t,
        "ic_attrition_ctrl": np.round(ic_attr_ctrl_series, 2),
        "ic_attrition_treat": np.round(ic_attr_treat_series, 2),
        "domino_attrition_ctrl": np.round(domino_ctrl_series, 2),
        "domino_attrition_treat": np.round(domino_treat_treat_series, 2),
        "tech_fulfillment_ctrl": np.round(skill_decay_curve, 2),
        "tech_fulfillment_treat": np.round(skill_treat_curve, 2),
        "reskilled_treat": reskilled_treat,
        "reskilled_ctrl": reskilled_ctrl,
        "cum_rework_loss_ctrl": np.round(cum_rework_loss_ctrl, 1),
        "cum_rework_defense_treat": np.round(cum_rework_defense_treat, 1),
        "hcroi_ctrl": np.round(hcroi_ctrl_series, 2),
        "hcroi_treat": np.round(hcroi_treat_series, 2),
        "net_financial_ctrl": np.round(net_fin_ctrl, 1),
        "net_financial_treat": np.round(net_fin_treat, 1)
    })
    
    # Terminal Agent States at month 60
    agents_ctrl = df_pop.copy()
    agents_treat = df_pop.copy()
    
    rng = np.random.default_rng(seed)
    
    # --- CONTROL GROUP AGENT BEHAVIOR ---
    ctrl_tracks = []
    ctrl_fits = []
    ctrl_skills = []
    ctrl_statuses = []
    ctrl_flights = []
    ctrl_losses = []
    
    for idx, row in agents_ctrl.iterrows():
        ic = row["ic_propensity"]
        mgr = row["mgr_propensity"]
        tenure = row["tenure"]
        base_skill = row["initial_skill"]
        
        # Peter Principle: In Control, high tenure agents get forced into Manager track
        is_forced_mgr = (tenure >= 6 and rng.random() < control_forced_mgr_rate)
        if is_forced_mgr:
            track = "Manager"
            fit = mgr  # fit is low if mgr propensity is low
        else:
            track = "IC" if ic >= mgr else "Manager"
            fit = ic if track == "IC" else mgr
            
        # Skill decay without dynamic reskilling
        final_skill = float(np.clip(base_skill * (target_tech_ctrl / 88.4) + rng.normal(0, 4), 25, 95))
        
        # Flight risk computation
        is_mismatch = (track == "Manager" and ic > 0.65 and mgr < 0.45)
        if row["emp_id"] == "EMP-042":
            is_mismatch = True
            flight_risk = 0.84
            status = "번아웃·이탈위험"
            loss = 4.2
        elif is_mismatch:
            flight_risk = float(np.clip(0.70 + rng.uniform(0.05, 0.22), 0.70, 0.95))
            loss = float(np.round(rng.uniform(2.5, 4.8), 1))
            status = "피터의 법칙 부조화" if flight_risk < 0.80 else "번아웃·이탈위험"
        else:
            flight_risk = float(np.clip(0.15 + (1.0 - fit) * 0.35 + rng.normal(0, 0.05), 0.05, 0.65))
            loss = float(np.round(rng.uniform(0.8, 2.2), 1))
            status = "정상 재직"
            
        # Attrition thresholding to match cumulative attrition rate
        if rng.random() < (target_ic_attr_ctrl / 100.0) * (0.6 if not is_mismatch else 1.5):
            status = "퇴사 (Attrition)"
            
        ctrl_tracks.append(track)
        ctrl_fits.append(np.round(fit, 2))
        ctrl_skills.append(np.round(final_skill, 1))
        ctrl_statuses.append(status)
        ctrl_flights.append(np.round(flight_risk, 2))
        ctrl_losses.append(loss)
        
    agents_ctrl["track"] = ctrl_tracks
    agents_ctrl["fit_score"] = ctrl_fits
    agents_ctrl["current_skill"] = ctrl_skills
    agents_ctrl["status"] = ctrl_statuses
    agents_ctrl["flight_risk"] = ctrl_flights
    agents_ctrl["expected_loss"] = ctrl_losses
    
    # --- TREATMENT GROUP AGENT BEHAVIOR ---
    treat_tracks = []
    treat_fits = []
    treat_skills = []
    treat_statuses = []
    treat_flights = []
    treat_losses = []
    
    for idx, row in agents_treat.iterrows():
        ic = row["ic_propensity"]
        mgr = row["mgr_propensity"]
        base_skill = row["initial_skill"]
        
        # Treatment: Module 1 dynamic track matching
        if ic >= mgr:
            track = "IC"
            fit = ic
            status = "전문가(IC) 안착"
        else:
            track = "Manager"
            fit = mgr
            status = "관리자(MGR) 안착"
            
        # Career pivot cases (agents with minor gap who pivoted smoothly)
        if abs(ic - mgr) < 0.12 and row["tenure"] >= 5:
            status = "커리어 피벗 완료"
            fit = max(ic, mgr) * 0.95
            
        # Reskilling keeps skills high
        final_skill = float(np.clip(base_skill * (target_tech_treat / 90.0) + rng.normal(0, 3), 70, 100))
        
        # Low flight risk due to proper matching, veto rights, and royalty
        flight_risk = float(np.clip(0.08 + (1.0 - fit) * 0.12 + rng.normal(0, 0.03), 0.04, 0.35))
        loss = float(np.round(rng.uniform(1.2, 3.5), 1))
        
        # EMP-042 in Treatment: Successfully pivoted to L6 Staff IC with low risk!
        if row["emp_id"] == "EMP-042":
            track = "IC"
            fit = 0.91
            status = "커리어 피벗 완료"
            flight_risk = 0.14
            loss = 4.2
            
        # Low attrition rate
        if rng.random() < (target_ic_attr_treat / 100.0) * 0.6:
            status = "퇴사 (최소화)"
            
        treat_tracks.append(track)
        treat_fits.append(np.round(fit, 2))
        treat_skills.append(np.round(final_skill, 1))
        treat_statuses.append(status)
        treat_flights.append(np.round(flight_risk, 2))
        treat_losses.append(loss)
        
    agents_treat["track"] = treat_tracks
    agents_treat["fit_score"] = treat_fits
    agents_treat["current_skill"] = treat_skills
    agents_treat["status"] = treat_statuses
    agents_treat["flight_risk"] = treat_flights
    agents_treat["expected_loss"] = treat_losses
    
    # Summary Metrics Dictionary
    summary = {
        "ctrl_ic_attrition": np.round(target_ic_attr_ctrl, 1),
        "treat_ic_attrition": np.round(target_ic_attr_treat, 1),
        "ctrl_domino_attrition": np.round(target_domino_ctrl, 1),
        "treat_domino_attrition": np.round(target_domino_treat, 1),
        "ctrl_tech_fulfillment": np.round(target_tech_ctrl, 1),
        "treat_tech_fulfillment": np.round(target_tech_treat, 1),
        "ctrl_recovery_time": np.round(target_rec_ctrl, 1),
        "treat_recovery_time": np.round(target_rec_treat, 1),
        "ctrl_rework_loss": np.round(target_rework_loss_ctrl, 1),
        "treat_rework_defense": np.round(target_rework_defense_treat, 1),
        "ctrl_hcroi": np.round(target_hcroi_ctrl, 2),
        "treat_hcroi": np.round(target_hcroi_treat, 2),
        "ctrl_retention_rate": np.round(100.0 - target_ic_attr_ctrl, 1),
        "treat_retention_rate": np.round(100.0 - target_ic_attr_treat, 1),
        "ctrl_avg_skill": np.round(agents_ctrl["current_skill"].mean(), 1),
        "treat_avg_skill": np.round(agents_treat["current_skill"].mean(), 1),
        "ctrl_net_financial": np.round(net_fin_ctrl[-1], 1),
        "treat_net_financial": np.round(net_fin_treat[-1], 1)
    }
    
    return summary, timeseries_df, agents_ctrl, agents_treat

# --- Helper Functions for Tab 4, 5, 6 ---

def get_top_flight_risk(agents_ctrl_df, top_n=10):
    """Extracts top flight risk agents for Tab 4 Early Warning Radar."""
    high_risks = agents_ctrl_df[agents_ctrl_df["status"].isin(["피터의 법칙 부조화", "번아웃·이탈위험"])].copy()
    high_risks = high_risks.sort_values(by="flight_risk", ascending=False).head(top_n)
    
    # Reasons mapping
    reasons = []
    for idx, row in high_risks.iterrows():
        if row["track"] == "Manager" and row["ic_propensity"] > 0.7:
            reasons.append("피터의 법칙 부조화 (관리직 강제배치)")
        elif row["current_skill"] < 60:
            reasons.append("기술 노후화 및 직무 정체")
        else:
            reasons.append("외부 시장 몸값 격차 (스카우트)")
    high_risks["cause"] = reasons
    return high_risks

def simulate_retention_prescription(emp_id="EMP-042", initial_risk=0.84, initial_loss=4.2):
    """Simulates 3 Retention Packages for a specific high-risk talent."""
    return [
        {
            "package_name": "오퍼 ①: L6 수석 전문가 피벗 + 브릿지 러닝 + 독립 AI 서버 배정",
            "risk_after": 14.0,
            "cost": 0.4,
            "net_gain": round(initial_loss * (1 - 0.14) - 0.4, 2),
            "recommendation": "최적 추천 (IC 성향 91% 회복 및 RAG 자산화 유도)"
        },
        {
            "package_name": "오퍼 ②: 외부 시장 가치 보전 수당 핀셋 12% 인상 (현 트랙 유지)",
            "risk_after": 52.0,
            "cost": 0.5,
            "net_gain": round(initial_loss * (1 - 0.52) - 0.5, 2),
            "recommendation": "단기 임시방편 (직무 부조화 스트레스 미해소)"
        },
        {
            "package_name": "오퍼 ③: 현 상태 유지 (Status Quo - 관리직 지속)",
            "risk_after": round(initial_risk * 100, 1),
            "cost": 0.0,
            "net_gain": 0.0,
            "recommendation": "이탈 확실시 (예상 대체·공백 손실 4.2억 원 전액 발생)"
        }
    ]

def compute_policy_sandbox_matrix(reskill_eff=0.85, veto_on=True):
    """
    Computes 7x7 grid of RAG Royalty Rate (1~7%) x L6 Promotion Cutoff (2~5억)
    Returns retention rate and budget compliance flag.
    """
    royalties = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
    cutoffs = [2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
    
    data = []
    for c in cutoffs:
        row = []
        for r in royalties:
            # Retention increases with royalty, optimal around 3.5~4.5%, drops if cutoff is too high
            retention = 78.0 + 3.0 * (r ** 0.6) - 2.5 * abs(c - 3.5) + (reskill_eff - 0.85) * 10.0
            if not veto_on:
                retention -= 4.0
            retention = float(np.clip(retention, 65.0, 94.5))
            
            # Budget compliant if royalty <= 5.0% or cutoff >= 3.0
            budget_ok = not (r > 5.0 and c < 3.0)
            row.append({
                "royalty": r,
                "cutoff": c,
                "retention": round(retention, 1),
                "budget_ok": budget_ok,
                "is_sweet_spot": (3.5 <= r <= 4.5 and 3.0 <= c <= 4.0)
            })
        data.append(row)
    return royalties, cutoffs, data

def compute_workforce_planning(target_headcount=40, tech_domain="AI 아키텍트 및 MLOps", reskill_eff=0.85):
    """Computes Build vs Buy optimization for Tab 5."""
    build_ratio = np.clip(0.70 * (reskill_eff / 0.85), 0.50, 0.85)
    build_count = int(round(target_headcount * build_ratio))
    buy_count = target_headcount - build_count
    
    # Financials (in 억원)
    build_cost_per_person = 0.10  # 1,000만원
    buy_cost_per_person = 0.80    # 8,000만원 (헤드헌팅, 인터뷰, 온보딩 공백)
    
    build_total = round(build_count * build_cost_per_person, 1)
    buy_total = round(buy_count * buy_cost_per_person, 1)
    hybrid_total = round(build_total + buy_total, 1)
    
    all_buy_total = round(target_headcount * buy_cost_per_person, 1)
    saved_total = round(all_buy_total - hybrid_total, 1)
    savings_pct = round((saved_total / all_buy_total) * 100, 1)
    
    return {
        "target_headcount": target_headcount,
        "domain": tech_domain,
        "build_count": build_count,
        "buy_count": buy_count,
        "build_total": build_total,
        "buy_total": buy_total,
        "hybrid_total": hybrid_total,
        "all_buy_total": all_buy_total,
        "saved_total": saved_total,
        "savings_pct": savings_pct
    }

def compute_tf_chemistry(mgr_id="MGR-12 박준영", ic_id="IC-08 강동훈"):
    """Computes 5-dimension TF Chemistry radar scores."""
    # Presets for predictable demo consistency
    scores_map = {
        ("MGR-12 박준영", "IC-08 강동훈"): [94, 91, 93, 88, 92],
        ("MGR-12 박준영", "IC-14 송지우"): [88, 85, 90, 82, 86],
        ("MGR-05 최민호", "IC-08 강동훈"): [82, 74, 85, 78, 80],
        ("MGR-05 최민호", "IC-14 송지우"): [91, 89, 88, 86, 90]
    }
    
    scores = scores_map.get((mgr_id, ic_id), [88, 84, 89, 85, 87])
    composite = round(np.mean(scores), 1)
    
    dimensions = [
        "기술-일정 조율 시너지",
        "결재권 분리 수용도",
        "팀원 재숙련 육성 지수",
        "의사결정 속도",
        "프로젝트 완수 확률"
    ]
    
    veto_conflict_risk = round(100 - scores[1], 1)
    delay_risk = round(100 - scores[3], 1)
    
    return {
        "dimensions": dimensions,
        "scores": scores,
        "composite": composite,
        "veto_conflict_risk": veto_conflict_risk,
        "delay_risk": delay_risk,
        "verdict": "탁월한 시너지: 수석 전문가의 기술적 엄격함과 관리자의 애자일 조율 역량이 조화를 이루어 대형 전략 TF 성공 가능성 최상." if composite >= 90 else "양호한 시너지: 안건별 결재권 사전 합의를 통해 일정 지연 리스크 방어 권고."
    }

def get_employee_persona_profile(emp_id="EMP-108", royalty_rate=0.04):
    """Retrieves single employee profile for Tab 6 XAI My Career Simulator."""
    if emp_id == "EMP-108":
        return {
            "emp_id": "EMP-108",
            "name": "이서진",
            "level": "L5",
            "title": "책임 / 시니어 전문가 (Senior IC)",
            "tenure": 7,
            "ic_prop": 89,
            "mgr_prop": 28,
            "primary_skill": "클라우드 네이티브 & 분산 백엔드",
            "decay_half_life_years": 1.8,
            "decay_risk_pct": 32,
            "rag_assets": 12,
            "rag_reuses": 142,
            "hours_saved": 1136,
            "royalty_earned_manwon": int(round(1136 * 50000 * royalty_rate / 10000 + 1620)),
            "influence_score": 94.2,
            "current_base_salary": 9800,  # 만원
            "rec_courses": [
                {"title": "클라우드 네이티브 AI 인프라 및 LLMOps 분산 서빙", "match_pct": 94, "weeks": 6},
                {"title": "RAG 파이프라인 최적화 및 벡터 임베딩 튜닝", "match_pct": 89, "weeks": 4}
            ]
        }
    elif emp_id == "EMP-042":
        return {
            "emp_id": "EMP-042",
            "name": "김도윤",
            "level": "L6",
            "title": "팀장 (Team Manager)",
            "tenure": 9,
            "ic_prop": 91,
            "mgr_prop": 24,
            "primary_skill": "대규모 데이터 엔지니어링 & 파이프라인",
            "decay_half_life_years": 1.4,
            "decay_risk_pct": 48,
            "rag_assets": 8,
            "rag_reuses": 98,
            "hours_saved": 784,
            "royalty_earned_manwon": int(round(784 * 50000 * royalty_rate / 10000 + 850)),
            "influence_score": 92.5,
            "current_base_salary": 11500,
            "rec_courses": [
                {"title": "L6 수석 전문가 복귀를 위한 테크 리프레시 부트캠프", "match_pct": 98, "weeks": 4},
                {"title": "차세대 분산 스트리밍 & 실시간 AI 파이프라인 아키텍처", "match_pct": 92, "weeks": 6}
            ]
        }
    else:
        # Default fallback persona EMP-215
        return {
            "emp_id": "EMP-215",
            "name": "박지훈",
            "level": "L5",
            "title": "파트장 (Part Lead)",
            "tenure": 6,
            "ic_prop": 32,
            "mgr_prop": 86,
            "primary_skill": "애자일 프로젝트 관리 & 조직 조율",
            "decay_half_life_years": 3.2,
            "decay_risk_pct": 18,
            "rag_assets": 4,
            "rag_reuses": 45,
            "hours_saved": 360,
            "royalty_earned_manwon": 450,
            "influence_score": 86.8,
            "current_base_salary": 9500,
            "rec_courses": [
                {"title": "L6 팀장 승격을 위한 AI 기반 프로젝트 병목 분석 및 위임 리더십", "match_pct": 96, "weeks": 4},
                {"title": "팀원 맞춤형 재숙련 코칭 및 AI 1on1 면담 실습", "match_pct": 91, "weeks": 3}
            ]
        }
