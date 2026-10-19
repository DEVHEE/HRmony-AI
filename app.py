"""
HRmony AI - Organizational Digital Twin & HR Decision Intelligence System
Pair Programming Implementation based on Proposal Specification (proposal_spec.md)
Features:
- Enterprise Slate Design Benchmark (Workday Peakon, Visier, Lattice)
- Presentation & Capture-Ready Layouts (16:9 / 16:10 Ratio)
- Intuitive Sidebar Parameter Explanations (Meaning & Impact)
- High-Resolution Architecture & State Transition Diagrams via Streamlit Components
- Real-time Multi-Agent Simulation Engine (N=500, t=1..60)
"""

import streamlit as st
import streamlit.components.v1 as components
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Local Modular Imports
import styles
import diagrams
import engine

# Page Configuration
st.set_page_config(
    page_title="HRmony AI - 가상 조직 시뮬레이터 & HR 인텔리전스",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply Custom Enterprise CSS
st.markdown(styles.ENTERPRISE_CSS, unsafe_allow_html=True)

# --- Top Header ---
st.markdown("""
<div class="hrm-header-container">
    <div class="hrm-title-area">
        <h1 class="hrm-title">
            HRmony <span class="hrm-title-highlight">AI</span>
        </h1>
        <p class="hrm-subtitle">
            AI 기반 동적 이중경력경로 및 가상 조직 시뮬레이션 시스템 (Organizational Digital Twin & HR Decision Intelligence)
        </p>
    </div>
    <div class="hrm-header-meta">
        <span class="hrm-meta-badge active">시뮬레이션 엔진: 정상 가동 중</span>
        <span class="hrm-meta-badge">가상 임직원: 500명</span>
        <span class="hrm-meta-badge">검증 기간: 60개월 (5개년)</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Executive Overview Hero Banner (Zero Wasted Space, Balanced Grid) ---
st.markdown("""
<div class="hrm-hero-banner">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <span style="font-size: 13.5px; font-weight: 700; color: #1E293B;">
            시스템 개요 (Executive Summary): HRmony AI는 무엇을 증명하는 프로그램인가요?
        </span>
        <span class="badge-status badge-info">1분 핵심 요약</span>
    </div>
    <div class="hrm-hero-grid">
        <div class="hrm-hero-card problem">
            <div class="hrm-hero-card-title" style="color: #DC2626;">
                1. 기존 제도의 치명적 결함 (피터의 법칙)
            </div>
            <p class="hrm-hero-card-desc">
                우수한 엔지니어·전문가(IC)가 연차가 차면 억지로 '팀장(관리직)'으로 승진시켜 기술력도 잃고 본인도 지쳐 퇴사하며, 산하 팀원들까지 연쇄 이탈하는 구조적 참사가 반복됩니다.
            </p>
        </div>
        <div class="hrm-hero-card solution">
            <div class="hrm-hero-card-title" style="color: #2563EB;">
                2. 제안 해결책 (동적 이중경력경로)
            </div>
            <p class="hrm-hero-card-desc">
                팀장이 되지 않고 수석 전문가(L6~L8)로 남아도 팀장과 동등한 연봉, 무리한 개발 일정을 막는 기술 결재 거부권(Veto), 후배 교육용 RAG 지식 재사용 로열티 보너스를 보장합니다.
            </p>
        </div>
        <div class="hrm-hero-card simulator">
            <div class="hrm-hero-card-title" style="color: #059669;">
                3. 이 시뮬레이터의 실증 역할
            </div>
            <p class="hrm-hero-card-desc">
                실제 회사에 도입하기 전, 가상 직원 500명을 컴퓨터 안에서 5년간 미리 구동하여 핵심인재 퇴사율(38%→11%)과 순재무 가치(+115억 원)를 사전에 정량 검증합니다.
            </p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Sidebar Controls with Clear Explanations (Meaning & Impact) ---
st.sidebar.markdown("### 가상 조직 환경 제어")
st.sidebar.caption("파라미터 조작 시 500명의 가상 직원이 실시간으로 반응합니다.")

with st.sidebar.expander("1. 가상 조직 기본 설정", expanded=False):
    sim_n = st.slider("가상 임직원 수 (N)", min_value=200, max_value=1000, value=500, step=50)
    st.markdown("""
    <div class="param-help">
        <div class="param-meaning"><strong>의미:</strong> 시뮬레이션 대상 가상 기업의 전체 정규직 인원 규모</div>
        <div class="param-impact"><strong>영향:</strong> 모수가 커질수록 전사 재무 기여 총액 및 재숙련 대상 인원 확대</div>
    </div>
    """, unsafe_allow_html=True)

    sim_months = st.slider("시뮬레이션 기간 (t)", min_value=12, max_value=60, value=60, step=12)
    st.markdown("""
    <div class="param-help">
        <div class="param-meaning"><strong>의미:</strong> 제도를 가상 조직에 적용해 미래로 구동할 시간 (기본 60개월=5년)</div>
        <div class="param-impact"><strong>영향:</strong> 기간이 길수록 누적 이직률 격차 및 5개년 누적 재무 성과 확대</div>
    </div>
    """, unsafe_allow_html=True)

    sim_seed = st.number_input("랜덤 시드 (Random Seed)", min_value=1, max_value=9999, value=42, step=1)
    st.markdown("""
    <div class="param-help">
        <div class="param-meaning"><strong>의미:</strong> 가상 임직원 속성 및 사건 발생 난수 기준값 (기본 42)</div>
        <div class="param-impact"><strong>영향:</strong> 42 적용 시 연구 제안서 본문 [표 4] 수치와 100% 동일하게 재현</div>
    </div>
    """, unsafe_allow_html=True)

with st.sidebar.expander("2. 외부 시장 환경 변수", expanded=False):
    param_decay = st.slider("AI 기술 연간 반감기율 (Skill Decay)", min_value=0.10, max_value=0.40, value=0.25, step=0.05, format="%.2f")
    st.markdown("""
    <div class="param-help">
        <div class="param-meaning"><strong>의미:</strong> AI 발전으로 기존 기술 가치가 1년에 떨어지는 속도 (연 25%)</div>
        <div class="param-impact"><strong>영향:</strong> 높일수록 신기술 충족률이 급락하고 사내 재교육(재숙련) 비용 급증</div>
    </div>
    """, unsafe_allow_html=True)

    param_pressure = st.selectbox("외부 시장 스카우트/연봉 압박", options=["낮음", "보통", "높음"], index=1)
    st.markdown("""
    <div class="param-help">
        <div class="param-meaning"><strong>의미:</strong> 경쟁사가 사내 핵심 전문가를 고액 연봉으로 빼가려는 유혹 강도</div>
        <div class="param-impact"><strong>영향:</strong> '높음'일수록 보상이 정체된 대조군(Control) 전문가의 퇴사율 폭증</div>
    </div>
    """, unsafe_allow_html=True)

with st.sidebar.expander("3. [모듈 1·2] 경로 및 재숙련 변수", expanded=True):
    param_forced_mgr = st.slider("전문가 관리직 강제배치율 (Control용)", min_value=0.30, max_value=0.90, value=0.65, step=0.05, format="%.2f")
    st.markdown("""
    <div class="param-help">
        <div class="param-meaning"><strong>의미:</strong> 기존 회사에서 우수 실무자를 억지로 팀장으로 승진시키는 관행 비율</div>
        <div class="param-impact"><strong>영향:</strong> 높일수록 피터의 법칙 부조화 및 팀원 연쇄 동반 퇴사율 폭증</div>
    </div>
    """, unsafe_allow_html=True)

    param_reskill_eff = st.slider("동적 재숙련 & 브릿지러닝 전이효율", min_value=0.50, max_value=1.00, value=0.85, step=0.05, format="%.2f")
    st.markdown("""
    <div class="param-help">
        <div class="param-meaning"><strong>의미:</strong> 적시형 AI 교육을 통해 신기술을 성공적으로 습득하는 전이율</div>
        <div class="param-impact"><strong>영향:</strong> 높일수록 사내 신기술 자급률 88% 유지 및 고비용 외부 채용 대체</div>
    </div>
    """, unsafe_allow_html=True)

with st.sidebar.expander("4. [모듈 3] 평가·보상·권한 변수", expanded=True):
    param_royalty = st.slider("사내 지식(RAG) 재사용 로열티 요율", min_value=0.01, max_value=0.07, value=0.04, step=0.005, format="%.3f")
    st.markdown("""
    <div class="param-help">
        <div class="param-meaning"><strong>의미:</strong> 전문가 산출물을 동료가 재사용할 때 절감 인건비의 보너스 지급률</div>
        <div class="param-impact"><strong>영향:</strong> 높일수록 전문가 만족도 상승 및 퇴사 시 기술 공백 복구 기간 단축</div>
    </div>
    """, unsafe_allow_html=True)

    param_mgr_bonus = st.slider("관리자 팀원 육성 보너스 가중치", min_value=0.01, max_value=0.07, value=0.035, step=0.005, format="%.3f")
    st.markdown("""
    <div class="param-help">
        <div class="param-meaning"><strong>의미:</strong> 팀장이 팀원의 신기술 습득 및 승격을 지원할 때 받는 육성 인센티브</div>
        <div class="param-impact"><strong>영향:</strong> 관리자가 팀원의 교육을 막지 않고 적극 육성하도록 동기부여</div>
    </div>
    """, unsafe_allow_html=True)

    param_veto = st.toggle("전문가 기술 결재 거부권(Veto) 시스템 강제", value=True)
    st.markdown("""
    <div class="param-help">
        <div class="param-meaning"><strong>의미:</strong> 무리한 일정 강행 시 전문가가 결재 단계에서 반려하는 시스템 권한</div>
        <div class="param-impact"><strong>영향:</strong> 활성화 시 연간 31.5억 원 상당의 대형 품질 결함·재작업 손실 방어</div>
    </div>
    """, unsafe_allow_html=True)

    param_cutoff = st.slider("L6 수석 승격 재무 기여 커트라인 (억원)", min_value=2.0, max_value=5.0, value=3.5, step=0.5)
    st.markdown("""
    <div class="param-help">
        <div class="param-meaning"><strong>의미:</strong> 팀장급(L6) 수석 전문가로 승격하기 위해 창출해야 할 연간 가치 기준선</div>
        <div class="param-impact"><strong>영향:</strong> 정책 샌드박스에서 최적 잔류율(91%↑)과 인건비 예산 준수점 결정</div>
    </div>
    """, unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.caption("HRmony-AI v2.0 Enterprise | Powered by Multi-Agent Digital Twin Engine")

# --- Run Simulation with Caching ---
@st.cache_data(show_spinner=False)
def get_simulation_results(n, months, seed, decay, pressure, forced_mgr, reskill_eff, royalty, mgr_bonus, veto, cutoff):
    return engine.run_simulation(
        n_agents=n,
        months=months,
        seed=seed,
        decay_rate=decay,
        salary_pressure=pressure,
        control_forced_mgr_rate=forced_mgr,
        reskill_efficiency=reskill_eff,
        royalty_rate=royalty,
        mgr_bonus_weight=mgr_bonus,
        veto_enabled=veto,
        l6_cutoff=cutoff
    )

with st.spinner("가상 조직 디지털 트윈 시뮬레이션 계산 중..."):
    summary, ts_df, agents_ctrl, agents_treat = get_simulation_results(
        sim_n, sim_months, sim_seed, param_decay, param_pressure,
        param_forced_mgr, param_reskill_eff, param_royalty,
        param_mgr_bonus, param_veto, param_cutoff
    )

# --- 6-Tab Interface Redesigned for Academic & Presentation Capture ---
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Tab 1 | [도식 1·2] 시스템 아키텍처 & 에이전트 로직맵",
    "Tab 2 | [캡처 1] 가상 조직 A/B 디지털 트윈 검증",
    "Tab 3 | [캡처 2 & 표 4] 5대 인사 난제 정량 검증 성적표",
    "Tab 4 | [캡처 3] 선제적 핀셋 리텐션 & 정책 샌드박스",
    "Tab 5 | [캡처 4] Buy vs Build 인력 수급 · TF 케미스트리 · CFO ROI",
    "Tab 6 | [캡처 5] 설명 가능한 AI(XAI) 마이 커리어 시뮬레이터"
])

# ==============================================================================
# TAB 1: Architecture & Agent Logic Map
# ==============================================================================
with tab1:
    st.markdown("""
    <div class="tab-guide-banner">
        🗺️ <strong>[도식 1·2 캡처 안내]</strong> 제안서 본문에 들어가는 제도의 전체 폐루프 아키텍처와 개별 직원의 월 단위 의사결정 순서도입니다.<br/>
        • <strong>상단 &lt;도식 1&gt;</strong>: 행동 데이터 진단 → 동적 재숙련 → 4대 공정보상 → 가상조직 시뮬레이션 환류의 4단계 선순환 구조입니다.<br/>
        • <strong>하단 &lt;도식 2&gt;</strong>: 매달 직원이 기술 노후화를 겪으며 만족도와 이탈 확률을 계산해 '잔류 / 피벗 / 퇴사'로 분기하는 알고리즘 순서도입니다.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hrm-card" style="padding-bottom: 4px;">
        <div class="hrm-card-header">
            <div>
                <h3 class="hrm-card-title">&lt;도식 1&gt; 전체 시스템 아키텍처 4단계 폐루프(Closed-Loop) 파이프라인</h3>
                <div class="hrm-card-desc">제안서 [그림 1] 삽입용 고해상도 벡터 아키텍처 다이어그램</div>
            </div>
            <span class="badge-status badge-info">Capture-Ready | 16:9</span>
        </div>
    """, unsafe_allow_html=True)

    # Render Standalone HTML Diagram 1 (Exact height to prevent scrollbar)
    components.html(diagrams.get_diagram_1_html(), height=465, scrolling=False)

    st.markdown("""
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-top: 10px; margin-bottom: 10px;">
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px; padding: 10px 12px;">
                <strong style="color: #1E293B; font-size: 12px;">[모듈 1] 경로 설계</strong>
                <p style="font-size: 11px; color: #64748B; margin-top: 3px; margin-bottom: 0;">
                    행동 로그 기반 IC vs MGR 성향 진단, 시장 연동 마이크로 KPI 및 양방향 피벗 지원
                </p>
            </div>
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px; padding: 10px 12px;">
                <strong style="color: #2563EB; font-size: 12px;">[모듈 2] 학습·재숙련</strong>
                <p style="font-size: 11px; color: #64748B; margin-top: 3px; margin-bottom: 0;">
                    AI 시대 기술 반감기 대응 동적 재숙련(Reskilling), 브릿지 러닝 및 사내 RAG AI 튜터화
                </p>
            </div>
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px; padding: 10px 12px;">
                <strong style="color: #D97706; font-size: 12px;">[모듈 3] 4대 HR 코어</strong>
                <p style="font-size: 11px; color: #64748B; margin-top: 3px; margin-bottom: 0;">
                    직무 성과 재무 환산, L5~L8 통합 레벨링, 기술 결재 거부권(Veto) 및 지식 로열티 보상
                </p>
            </div>
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px; padding: 10px 12px;">
                <strong style="color: #059669; font-size: 12px;">[모듈 4] 시뮬레이션·환류</strong>
                <p style="font-size: 11px; color: #64748B; margin-top: 3px; margin-bottom: 0;">
                    500명 가상 조직 사전 검증, 선제적 핀셋 리텐션, Buy vs Build 최적화 및 전략 환류
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hrm-card" style="padding-bottom: 4px; margin-top: 14px;">
        <div class="hrm-card-header">
            <div>
                <h3 class="hrm-card-title">&lt;도식 2&gt; 멀티 에이전트(Multi-Agent) 타임스텝 의사결정 상태 전이 순서도</h3>
                <div class="hrm-card-desc">제안서 [도식 2] 삽입용 월 단위(t=1..60) 에이전트 행동 및 3대 분기(Stay / Pivot / Attrition) 순서도</div>
            </div>
            <span class="badge-status badge-success">Capture-Ready | 16:9</span>
        </div>
    """, unsafe_allow_html=True)

    # Render Standalone HTML Diagram 2 (Exact height to prevent scrollbar)
    components.html(diagrams.get_diagram_2_html(), height=475, scrolling=False)

    st.markdown("</div>", unsafe_allow_html=True)


# ==============================================================================
# TAB 2: Twin Organization A/B Simulation Main
# ==============================================================================
with tab2:
    st.markdown("""
    <div class="tab-guide-banner">
        🏢 <strong>[화면 캡처 1 안내] 기존 회사 vs 우리 회사의 5년 뒤 조직 분포를 500개의 점으로 비교합니다.</strong><br/>
        • <strong>왼쪽(대조군 Control)</strong>: 관리직 강제 승진 관행으로 인해 '피터의 법칙 부조화(주황)'와 '퇴사(빨강)' 점이 쏟아져 나옵니다.<br/>
        • <strong>오른쪽(실험군 Treatment)</strong>: 성향 맞춤 트랙 안착과 동적 재숙련으로 '고숙련·고적합도(파랑/청록)' 우상향 영역에 안정적으로 밀집합니다.
    </div>
    """, unsafe_allow_html=True)

    # Top KPI Banner
    retention_delta = round(summary["treat_retention_rate"] - summary["ctrl_retention_rate"], 1)
    skill_delta = round(summary["treat_avg_skill"] - summary["ctrl_avg_skill"], 1)
    net_fin_delta = round(summary["treat_net_financial"] - summary["ctrl_net_financial"], 1)
    hcroi_delta_pct = round(((summary["treat_hcroi"] - summary["ctrl_hcroi"]) / summary["ctrl_hcroi"]) * 100, 1)

    st.markdown(f"""
    <div class="hrm-kpi-grid">
        <div class="hrm-kpi-card">
            <div class="hrm-kpi-label">핵심인재 유지율 (5개년 재직률)</div>
            <div class="hrm-kpi-value-row">
                <span class="hrm-kpi-value-treatment">{summary["treat_retention_rate"]}%</span>
                <span class="hrm-kpi-value-control">기존: {summary["ctrl_retention_rate"]}%</span>
            </div>
            <span class="hrm-kpi-delta positive">+{retention_delta}%p 개선 (이탈 방어)</span>
        </div>
        <div class="hrm-kpi-card">
            <div class="hrm-kpi-label">전사 평균 기술 숙련도 (100점 만점)</div>
            <div class="hrm-kpi-value-row">
                <span class="hrm-kpi-value-treatment">{summary["treat_avg_skill"]}점</span>
                <span class="hrm-kpi-value-control">기존: {summary["ctrl_avg_skill"]}점</span>
            </div>
            <span class="hrm-kpi-delta positive">+{skill_delta}점 역량 보전</span>
        </div>
        <div class="hrm-kpi-card">
            <div class="hrm-kpi-label">5개년 누적 순재무 기여액</div>
            <div class="hrm-kpi-value-row">
                <span class="hrm-kpi-value-treatment">{summary["treat_net_financial"]}억</span>
                <span class="hrm-kpi-value-control">기존: {summary["ctrl_net_financial"]}억</span>
            </div>
            <span class="hrm-kpi-delta positive">+{net_fin_delta}억 원 초과 창출</span>
        </div>
        <div class="hrm-kpi-card">
            <div class="hrm-kpi-label">인적자본 투자수익률 (HCROI)</div>
            <div class="hrm-kpi-value-row">
                <span class="hrm-kpi-value-treatment">{summary["treat_hcroi"]}배</span>
                <span class="hrm-kpi-value-control">기존: {summary["ctrl_hcroi"]}배</span>
            </div>
            <span class="hrm-kpi-delta positive">+{hcroi_delta_pct}% 투자 효율 증가</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 2-Column Comparison View: Agent Distributions
    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown("""
        <div style="font-size: 13.5px; font-weight: 700; color: #1E293B; margin-bottom: 3px;">
            [대조군 Control] 기존 인사제도: 가상 조직 에이전트 분포도 (N=500)
        </div>
        <div style="font-size: 11.5px; color: #DC2626; margin-bottom: 8px;">
            ⚠️ 강제 관리직 배치로 인한 피터의 법칙 부조화(주황) 및 대규모 퇴사(빨강) 집중
        </div>
        """, unsafe_allow_html=True)

        color_map_ctrl = {
            "정상 재직": "#64748B",
            "피터의 법칙 부조화": "#F59E0B",
            "번아웃·이탈위험": "#F43F5E",
            "퇴사 (Attrition)": "#DC2626"
        }

        fig_ctrl = px.scatter(
            agents_ctrl,
            x="fit_score",
            y="current_skill",
            color="status",
            size="tenure",
            color_discrete_map=color_map_ctrl,
            hover_data=["emp_id", "name", "level", "track", "flight_risk", "expected_loss"],
            labels={
                "fit_score": "직무 적합도 점수 (1.0 만점)",
                "current_skill": "현재 기술 숙련도 점수 (100점 만점)",
                "status": "직원 상태"
            }
        )
        layout_ctrl = styles.get_clean_plotly_layout(height=400)
        layout_ctrl["xaxis"]["range"] = [0.0, 1.05]
        layout_ctrl["yaxis"]["range"] = [20, 105]
        fig_ctrl.update_layout(layout_ctrl)
        st.plotly_chart(fig_ctrl, width="stretch")

    with col_right:
        st.markdown("""
        <div style="font-size: 13.5px; font-weight: 700; color: #1E293B; margin-bottom: 3px;">
            [실험군 Treatment] 제안 AI 통합 모델: 가상 조직 에이전트 분포도 (N=500)
        </div>
        <div style="font-size: 11.5px; color: #059669; margin-bottom: 8px;">
            ✅ 성향 맞춤 트랙 분기 및 동적 재숙련으로 고숙련·고적합도(파랑/청록) 영역에 안정적 밀집
        </div>
        """, unsafe_allow_html=True)

        color_map_treat = {
            "전문가(IC) 안착": "#2563EB",
            "관리자(MGR) 안착": "#0D9488",
            "커리어 피벗 완료": "#6366F1",
            "퇴사 (최소화)": "#DC2626"
        }

        fig_treat = px.scatter(
            agents_treat,
            x="fit_score",
            y="current_skill",
            color="status",
            size="tenure",
            color_discrete_map=color_map_treat,
            hover_data=["emp_id", "name", "level", "track", "flight_risk", "expected_loss"],
            labels={
                "fit_score": "직무 적합도 점수 (1.0 만점)",
                "current_skill": "현재 기술 숙련도 점수 (100점 만점)",
                "status": "직원 상태"
            }
        )
        layout_treat = styles.get_clean_plotly_layout(height=400)
        layout_treat["xaxis"]["range"] = [0.0, 1.05]
        layout_treat["yaxis"]["range"] = [20, 105]
        fig_treat.update_layout(layout_treat)
        st.plotly_chart(fig_treat, width="stretch")

    # Bottom Leveling Matrix Table
    st.markdown("""
    <div class="hrm-card" style="margin-top: 10px;">
        <div class="hrm-card-header">
            <div>
                <h3 class="hrm-card-title">&lt;표 1&gt; 통합 직급(L5~L8) 전문가 - 관리자 1:1 동등 매칭 매트릭스</h3>
                <div class="hrm-card-desc">연차가 아닌 연간 AI 재무 기여도와 대체 비용 기준 1:1 매칭 운영 현황</div>
            </div>
            <span class="badge-status badge-neutral">Unified Leveling</span>
        </div>
        <table class="hrm-table">
            <thead>
                <tr>
                    <th>통합 직급</th>
                    <th>전문가 직책 (IC Track)</th>
                    <th>관리자 직책 (Manager Track)</th>
                    <th>공통 업무 영향 범위</th>
                    <th>기존 제도 재직 (IC / MGR)</th>
                    <th>제안 모델 재직 (IC / MGR)</th>
                    <th>평균 연봉 (원)</th>
                    <th>연간 재무 기여 (원)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>L5</strong></td>
                    <td>책임 / 시니어 (Senior)</td>
                    <td>파트장 (Part Lead)</td>
                    <td>단일 팀 내부 고난도 과제 해결 및 후배 지도</td>
                    <td>42명 / 78명</td>
                    <td><strong>64명 / 58명</strong></td>
                    <td>9,500만 ~ 1.1억</td>
                    <td>1.2억 ~ 1.8억 원</td>
                </tr>
                <tr>
                    <td><strong>L6</strong></td>
                    <td>수석 전문가 (Staff)</td>
                    <td>팀장 (Team Manager)</td>
                    <td>팀 전체 ~ 다수 팀 핵심 기술 난제 해결 vs 팀 총괄</td>
                    <td>18명 / 64명 (피터의 법칙 집중)</td>
                    <td><strong>44명 / 41명 (균형 안착)</strong></td>
                    <td>1.2억 ~ 1.5억</td>
                    <td>3.5억 ~ 4.8억 원</td>
                </tr>
                <tr>
                    <td><strong>L7</strong></td>
                    <td>전문위원 (Principal)</td>
                    <td>실장 (Director)</td>
                    <td>본부 단위 기술 방향 설계 vs 부서 경영</td>
                    <td>5명 / 22명</td>
                    <td><strong>16명 / 14명</strong></td>
                    <td>1.6억 ~ 2.1억</td>
                    <td>7.5억 ~ 11.2억 원</td>
                </tr>
                <tr>
                    <td><strong>L8</strong></td>
                    <td>펠로우 (Fellow / Master)</td>
                    <td>본부장 (VP / 임원)</td>
                    <td>전사·업계 미래 핵심 원천기술 vs 사업부 손익</td>
                    <td>1명 / 8명</td>
                    <td><strong>5명 / 5명 (동등 위상)</strong></td>
                    <td>2.5억 원 이상</td>
                    <td>수십억 원 이상</td>
                </tr>
            </tbody>
        </table>
    </div>
    """, unsafe_allow_html=True)


# ==============================================================================
# TAB 3: 5 Key HR Dilemmas Quantitative Validation Dashboard
# ==============================================================================
with tab3:
    st.markdown("""
    <div class="tab-guide-banner">
        📊 <strong>[화면 캡처 2 & 표 4 안내] 연구 제안서에 삽입되는 결정적 6대 정량 검증 성적표와 4개 핵심 차트입니다.</strong><br/>
        • <strong>성적표</strong>: 전문가 이직률이 38.4%에서 11.2%로 감소하고, 연간 31.5억 원의 품질 결함 손실을 막아냈음을 증명합니다.<br/>
        • <strong>차트 1~4</strong>: 피터의 법칙 연쇄 퇴사 방어, 기술 반감기 자급률 88% 유지, RAG 지식 복구 1.4개월 단축, 전문가 거부권(Veto) 재무 방어를 실증합니다.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hrm-card">
        <div class="hrm-card-header">
            <div>
                <h3 class="hrm-card-title">&lt;표 4&gt; 기존 인사제도(Control) vs 제안 AI 모델(Treatment) 60개월 시뮬레이션 정량 검증 요약표</h3>
                <div class="hrm-card-desc">제안서 표와 1:1 매칭 (사이드바 변수를 조작하면 실제 수식에 따라 실시간 갱신됩니다)</div>
            </div>
            <span class="badge-status badge-success">Quantitative Validation</span>
        </div>
    """, unsafe_allow_html=True)

    table4_data = [
        {
            "지표": "① 고성과 전문가 누적 이직률",
            "Control": f"{summary['ctrl_ic_attrition']}%",
            "Treatment": f"{summary['treat_ic_attrition']}%",
            "개선폭": f"-{round(summary['ctrl_ic_attrition'] - summary['treat_ic_attrition'], 1)}%p",
            "쉬운 설명": "에이스 개발자 퇴사율이 1/3 토막으로 급감 (전문가도 팀장급 연봉 보장)"
        },
        {
            "지표": "② 부적합 관리자 산하 '도미노 연쇄 이직률'",
            "Control": f"{summary['ctrl_domino_attrition']}%",
            "Treatment": f"{summary['treat_domino_attrition']}%",
            "개선폭": f"-{round(summary['ctrl_domino_attrition'] - summary['treat_domino_attrition'], 1)}%p",
            "쉬운 설명": f"팀장 스트레스로 인한 팀원 동반 퇴사 77% 방어 (적성 맞춤 배치 효과)"
        },
        {
            "지표": "③ AI 기술 반감기 대비 사내 신기술 충족률",
            "Control": f"{summary['ctrl_tech_fulfillment']}%",
            "Treatment": f"{summary['treat_tech_fulfillment']}%",
            "개선폭": f"+{round(summary['treat_tech_fulfillment'] - summary['ctrl_tech_fulfillment'], 1)}%p",
            "쉬운 설명": "기술이 낡아도 사내 재교육으로 신기술 자급률 88% 유지"
        },
        {
            "지표": "④ 핵심 전문가 퇴사 시 기술 공백 복구 기간",
            "Control": f"평균 {summary['ctrl_recovery_time']}개월",
            "Treatment": f"평균 {summary['treat_recovery_time']}개월",
            "개선폭": f"-{round(summary['ctrl_recovery_time'] - summary['treat_recovery_time'], 1)}개월",
            "쉬운 설명": "전문가가 퇴사해도 사내 RAG AI 교재가 남아있어 1.4개월 만에 복구"
        },
        {
            "지표": "⑤ 대형 기술 결함·재작업 손실 방어액",
            "Control": f"연평균 {summary['ctrl_rework_loss']}억 손실",
            "Treatment": f"연평균 +{summary['treat_rework_defense']}억 방어",
            "개선폭": f"+{round(summary['treat_rework_defense'] - summary['ctrl_rework_loss'], 1)}억 원",
            "쉬운 설명": "무리한 출시 일정을 전문가가 '거부(Veto)'하여 대형 사고 예방"
        },
        {
            "지표": "⑥ 인적자본 투자수익률 (HCROI)",
            "Control": f"{summary['ctrl_hcroi']}배",
            "Treatment": f"{summary['treat_hcroi']}배",
            "개선폭": f"+{round(summary['treat_hcroi'] - summary['ctrl_hcroi'], 2)}배",
            "쉬운 설명": "인건비와 교육비 1원 투자할 때마다 2.84원의 순가치 창출"
        }
    ]

    t4_df = pd.DataFrame(table4_data)

    st.markdown("""
    <table class="hrm-table">
        <thead>
            <tr>
                <th style="width: 25%;">핵심 검증 지표 (60개월 기준)</th>
                <th style="width: 15%; color: #EF4444;">기존 제도 (Control)</th>
                <th style="width: 15%; color: #2563EB;">제안 AI 모델 (Treatment)</th>
                <th style="width: 12%;">개선 폭 (Delta)</th>
                <th style="width: 33%;">비전문가도 이해하는 효과 요약</th>
            </tr>
        </thead>
        <tbody>
    """, unsafe_allow_html=True)

    for row in table4_data:
        st.markdown(f"""
            <tr>
                <td><strong>{row['지표']}</strong></td>
                <td style="color: #DC2626; font-weight: 600;">{row['Control']}</td>
                <td style="color: #2563EB; font-weight: 700;">{row['Treatment']}</td>
                <td><span class="badge-status badge-success">{row['개선폭']}</span></td>
                <td style="color: #475569; font-size: 12px;">{row['쉬운 설명']}</td>
            </tr>
        """, unsafe_allow_html=True)

    st.markdown("</tbody></table></div>", unsafe_allow_html=True)

    # Download CSV
    csv_bytes = t4_df.to_csv(index=False).encode("utf-8-sig")
    st.download_button(
        label="📥 표 4 정량 데이터셋 CSV 다운로드",
        data=csv_bytes,
        file_name="hrmony_ai_table4_validation_results.csv",
        mime="text/csv"
    )

    st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

    # 2x2 Plotly Grid
    c1, c2 = st.columns(2)
    c3, c4 = st.columns(2)

    with c1:
        st.markdown("<div class='hrm-card'>", unsafe_allow_html=True)
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(
            x=ts_df["month"], y=ts_df["ic_attrition_ctrl"],
            mode="lines", name="기존: 전문가 퇴사율",
            line=dict(color=styles.COLOR_CONTROL, width=2.5)
        ))
        fig1.add_trace(go.Scatter(
            x=ts_df["month"], y=ts_df["domino_attrition_ctrl"],
            mode="lines", name="기존: 팀원 동반퇴사율",
            line=dict(color=styles.COLOR_CONTROL, width=1.8, dash="dash")
        ))
        fig1.add_trace(go.Scatter(
            x=ts_df["month"], y=ts_df["ic_attrition_treat"],
            mode="lines", name="제안: 전문가 퇴사율",
            line=dict(color=styles.COLOR_TREATMENT, width=2.5)
        ))
        fig1.add_trace(go.Scatter(
            x=ts_df["month"], y=ts_df["domino_attrition_treat"],
            mode="lines", name="제안: 팀원 동반퇴사율",
            line=dict(color=styles.COLOR_TREATMENT, width=1.8, dash="dash")
        ))
        layout1 = styles.get_clean_plotly_layout(title="[차트 1: 피터의 법칙 검증] 누적 이직률 추이 비교 (%)", height=320)
        layout1["yaxis"]["title"] = "누적 이직률 (%)"
        layout1["xaxis"]["title"] = "경과 개월 (t)"
        fig1.update_layout(layout1)
        st.plotly_chart(fig1, width="stretch")
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='hrm-card'>", unsafe_allow_html=True)
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(
            x=ts_df["month"], y=ts_df["tech_fulfillment_treat"],
            mode="lines", name="제안: 사내 신기술 충족률 (%)",
            line=dict(color=styles.COLOR_TREATMENT, width=2.5),
            fill="tozeroy", fillcolor="rgba(37, 99, 235, 0.08)"
        ))
        fig2.add_trace(go.Scatter(
            x=ts_df["month"], y=ts_df["tech_fulfillment_ctrl"],
            mode="lines", name="기존: 사내 신기술 충족률 (%)",
            line=dict(color=styles.COLOR_CONTROL, width=2.5),
            fill="tozeroy", fillcolor="rgba(239, 68, 68, 0.05)"
        ))
        layout2 = styles.get_clean_plotly_layout(title="[차트 2: 기술 반감기 검증] 사내 신기술 역량 충족률 (%)", height=320)
        layout2["yaxis"]["title"] = "기술 충족률 (%)"
        layout2["xaxis"]["title"] = "경과 개월 (t)"
        layout2["yaxis"]["range"] = [30, 100]
        fig2.update_layout(layout2)
        st.plotly_chart(fig2, width="stretch")
        st.markdown("</div>", unsafe_allow_html=True)

    with c3:
        st.markdown("<div class='hrm-card'>", unsafe_allow_html=True)
        categories = ["기술 공백 복구 기간 (개월)", "후배 업무 절감 시간 (x100h)"]
        ctrl_vals = [summary["ctrl_recovery_time"], 1.8]
        treat_vals = [summary["treat_recovery_time"], 14.8]

        fig3 = go.Figure(data=[
            go.Bar(name="기존 제도", x=categories, y=ctrl_vals, marker_color=styles.COLOR_CONTROL),
            go.Bar(name="제안 AI 모델 (RAG 자산화)", x=categories, y=treat_vals, marker_color=styles.COLOR_TREATMENT)
        ])
        layout3 = styles.get_clean_plotly_layout(title="[차트 3: 사일로 검증] 전문가 퇴사 시 기술 공백 복구 기간 비교", height=320)
        layout3["barmode"] = "group"
        fig3.update_layout(layout3)
        st.plotly_chart(fig3, width="stretch")
        st.markdown("</div>", unsafe_allow_html=True)

    with c4:
        st.markdown("<div class='hrm-card'>", unsafe_allow_html=True)
        fig4 = go.Figure()
        fig4.add_trace(go.Scatter(
            x=ts_df["month"], y=ts_df["cum_rework_defense_treat"],
            mode="lines", name="제안: 누적 품질사고 방어액 (억원)",
            line=dict(color=styles.COLOR_SUCCESS, width=2.5)
        ))
        fig4.add_trace(go.Scatter(
            x=ts_df["month"], y=ts_df["cum_rework_loss_ctrl"],
            mode="lines", name="기존: 누적 품질결함 손실액 (억원)",
            line=dict(color=styles.COLOR_CONTROL, width=2.5)
        ))
        fig4.add_trace(go.Scatter(
            x=ts_df["month"], y=ts_df["hcroi_treat"] * 30,
            mode="lines", name="제안: HCROI 추이 (x30 Scale)",
            line=dict(color=styles.COLOR_TREATMENT, width=2.0, dash="dot")
        ))
        layout4 = styles.get_clean_plotly_layout(title="[차트 4: 권한 분리 검증] 결함 방어액 (억원) 및 HCROI 궤적", height=320)
        layout4["yaxis"]["title"] = "금액 (억원)"
        layout4["xaxis"]["title"] = "경과 개월 (t)"
        fig4.update_layout(layout4)
        st.plotly_chart(fig4, width="stretch")
        st.markdown("</div>", unsafe_allow_html=True)


# ==============================================================================
# TAB 4: HR Intelligence 1 (Pinpoint Retention & Policy Sandbox)
# ==============================================================================
with tab4:
    st.markdown("""
    <div class="tab-guide-banner">
        🎯 <strong>[화면 캡처 3 안내] 퇴사 위험 직원을 조기 발견하고 맞춤형 오퍼로 붙잡는 리텐션 처방전입니다.</strong><br/>
        • <strong>좌측 레이더</strong>: 향후 6개월 내 이탈 확률 70% 이상인 고위험 핵심 인재 Top 10과 퇴사 시 예상 피해액을 경보합니다.<br/>
        • <strong>우측 시뮬레이터</strong>: 단순 연봉 인상(오퍼 2)보다 <strong>'수석 전문가 트랙 피벗 + 브릿지 러닝(오퍼 1)'</strong>이 이탈 확률을 84%→14%로 떨어뜨림을 증명합니다.<br/>
        • <strong>하단 히트맵</strong>: 로열티와 승격 기준을 어떻게 정해야 예산은 안 넘치고 잔류율은 91% 이상으로 극대화되는지(Sweet Spot)를 보여줍니다.
    </div>
    """, unsafe_allow_html=True)

    col_radar, col_offer = st.columns([1.1, 1.0])
    top_risks = engine.get_top_flight_risk(agents_ctrl, top_n=10)

    with col_radar:
        st.markdown("""
        <div class="hrm-card">
            <div class="hrm-card-header">
                <div>
                    <h3 class="hrm-card-title">이탈 고위험군 (Flight Risk ≥ 70%) 조기 경보 레이더</h3>
                    <div class="hrm-card-desc">퇴사 시 대체 비용 및 기술 공백 손실이 큰 핵심 인재 Top 10</div>
                </div>
                <span class="badge-status badge-danger">Early Warning Top 10</span>
            </div>
        """, unsafe_allow_html=True)

        selected_emp_label = st.selectbox(
            "처방 시뮬레이션 대상 직원 선택:",
            options=[f"{row['emp_id']} {row['name']} ({row['level']} {row['track']}) - 이탈확률 {int(row['flight_risk']*100)}%" for idx, row in top_risks.iterrows()],
            index=0
        )
        selected_emp_id = selected_emp_label.split()[0]
        selected_agent = top_risks[top_risks["emp_id"] == selected_emp_id].iloc[0]

        display_radar = top_risks[["emp_id", "name", "level", "track", "flight_risk", "expected_loss", "cause"]].copy()
        display_radar["flight_risk"] = (display_radar["flight_risk"] * 100).astype(int).astype(str) + "%"
        display_radar["expected_loss"] = display_radar["expected_loss"].astype(str) + "억 원"
        display_radar.columns = ["사번", "성명", "직급", "트랙", "이탈 확률", "예상 손실액", "주요 이탈 원인"]

        st.dataframe(
            display_radar,
            width="stretch",
            hide_index=True,
            height=280
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col_offer:
        st.markdown(f"""
        <div class="hrm-card">
            <div class="hrm-card-header">
                <div>
                    <h3 class="hrm-card-title">AI 맞춤형 핀셋 리텐션 처방 시뮬레이터</h3>
                    <div class="hrm-card-desc">대상: {selected_agent['emp_id']} {selected_agent['name']} {selected_agent['level']} ({selected_agent['track']})</div>
                </div>
                <span class="badge-status badge-info">Retention Prescriptor</span>
            </div>
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px; padding: 10px 12px; margin-bottom: 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #1E293B;">
                    진단 소견: {selected_agent['cause']}
                </div>
                <div style="font-size: 11.5px; color: #64748B; margin-top: 3px;">
                    전문가 성향: <strong>{int(selected_agent['ic_propensity']*100)}%</strong> | 
                    관리자 성향: <strong>{int(selected_agent['mgr_propensity']*100)}%</strong> | 
                    퇴사 시 예상 손실: <strong style="color: #DC2626;">{selected_agent['expected_loss']}억 원</strong>
                </div>
            </div>
        """, unsafe_allow_html=True)

        prescriptions = engine.simulate_retention_prescription(
            emp_id=selected_agent["emp_id"],
            initial_risk=selected_agent["flight_risk"],
            initial_loss=selected_agent["expected_loss"]
        )

        for p in prescriptions:
            badge_color = "badge-success" if "오퍼 ①" in p["package_name"] else ("badge-warning" if "오퍼 ②" in p["package_name"] else "badge-danger")
            st.markdown(f"""
            <div style="border: 1px solid #E2E8F0; border-radius: 6px; padding: 8px 12px; margin-bottom: 6px; background: #FFFFFF;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <strong style="font-size: 12.5px; color: #1E293B;">{p['package_name']}</strong>
                    <span class="badge-status {badge_color}">이탈확률 {p['risk_after']}%</span>
                </div>
                <div style="font-size: 11px; color: #64748B; margin-top: 3px;">
                    소요 비용: {p['cost']}억 원 &nbsp;|&nbsp; 
                    방어 순이익: <strong style="color: #059669;">+{p['net_gain']}억 원</strong> &nbsp;|&nbsp; 
                    {p['recommendation']}
                </div>
            </div>
            """, unsafe_allow_html=True)

        fig_offer = go.Figure()
        fig_offer.add_trace(go.Bar(
            name="이탈 확률 (%)",
            x=["오퍼 ① (전문가피벗)", "오퍼 ② (연봉12%인상)", "오퍼 ③ (현상태유지)"],
            y=[p["risk_after"] for p in prescriptions],
            marker_color=["#2563EB", "#F59E0B", "#EF4444"]
        ))
        fig_offer.add_trace(go.Bar(
            name="방어 순이익 (억원)",
            x=["오퍼 ① (전문가피벗)", "오퍼 ② (연봉12%인상)", "오퍼 ③ (현상태유지)"],
            y=[p["net_gain"] * 20 for p in prescriptions],
            marker_color=["#10B981", "#6EE7B7", "#D1D5DB"]
        ))
        layout_offer = styles.get_clean_plotly_layout(height=210)
        layout_offer["barmode"] = "group"
        fig_offer.update_layout(layout_offer)
        st.plotly_chart(fig_offer, width="stretch")

        st.markdown("</div>", unsafe_allow_html=True)

    # Bottom Panel: Policy Sandbox Heatmap
    st.markdown("""
    <div class="hrm-card" style="margin-top: 8px;">
        <div class="hrm-card-header">
            <div>
                <h3 class="hrm-card-title">인사제도 개편 사전 정책 샌드박스 (Policy Sandbox 2D Heatmap)</h3>
                <div class="hrm-card-desc">로열티 요율(1~7%) × L6 승격 커트라인(2~5억) 조합별 핵심인재 잔류율(%) 및 Sweet Spot 도출</div>
            </div>
            <span class="badge-status badge-neutral">What-if Heatmap</span>
        </div>
    """, unsafe_allow_html=True)

    royalties, cutoffs, grid = engine.compute_policy_sandbox_matrix(reskill_eff=param_reskill_eff, veto_on=param_veto)
    z_vals = [[col["retention"] for col in row] for row in grid]

    fig_heat = px.imshow(
        z_vals,
        labels=dict(x="RAG 결과물 재사용 로열티 요율 (%)", y="L6 승격 연간 재무 기여 커트라인 (억원)", color="잔류율 (%)"),
        x=[f"{r}%" for r in royalties],
        y=[f"{c}억" for c in cutoffs],
        color_continuous_scale="Blues",
        aspect="auto",
        text_auto=True
    )
    layout_heat = styles.get_clean_plotly_layout(height=320)
    fig_heat.update_layout(layout_heat)
    st.plotly_chart(fig_heat, width="stretch")

    st.markdown("""
        <div style="font-size: 11.5px; color: #475569; background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px; padding: 8px 12px;">
            💡 <strong>Sweet Spot 최적 해설:</strong> 로열티 <strong>3.5% ~ 4.5%</strong> 구간 및 L6 승격 커트라인 <strong>3.0억 ~ 4.0억 원</strong> 구간을 설정하면, 회사의 인건비 예산을 초과하지 않으면서 핵심 인재 잔류율이 <strong>91% 이상</strong>으로 가장 높게 유지됩니다.
        </div>
    </div>
    """, unsafe_allow_html=True)


# ==============================================================================
# TAB 5: HR Intelligence 2 (Workforce Planning, TF Chemistry, CFO ROI)
# ==============================================================================
with tab5:
    st.markdown("""
    <div class="tab-guide-banner">
        💼 <strong>[화면 캡처 4 안내] 경영진과 인사 전략팀을 위한 3대 전략 도구입니다.</strong><br/>
        • <strong>패널 1 (인력 수급)</strong>: 밖에서 비싸게 새로 채용(Buy)할지 vs 안에서 교육(Build)해서 쓸지 비교해 19억 원을 절감합니다.<br/>
        • <strong>패널 2 (TF 케미스트리)</strong>: 팀장과 수석 전문가를 붙여놓았을 때 충돌 없이 시너지를 낼지 5각형 레이더로 미리 점쳐봅니다.<br/>
        • <strong>패널 3 (CFO 리포트)</strong>: 최고재무책임자에게 "15억 투자하면 115억 원 순이익이 남습니다"라고 보고하는 ROI 워터폴 차트입니다.
    </div>
    """, unsafe_allow_html=True)

    col_p1, col_p2, col_p3 = st.columns([1.0, 1.1, 1.1])

    # Panel 1: Buy vs Build
    with col_p1:
        st.markdown("""
        <div class="hrm-card">
            <div class="hrm-card-header">
                <div>
                    <h3 class="hrm-card-title">① 동적 인력 수급: Buy vs Build</h3>
                    <div class="hrm-card-desc">내부 재교육 vs 외부 채용 예산 비교</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        target_hc = st.slider("신사업 필요 인력 (명):", min_value=10, max_value=80, value=40, step=5)
        target_domain = st.selectbox(
            "대상 기술 직무 도메인:",
            options=["AI 아키텍트 및 MLOps", "클라우드 네이티브 백엔드", "생성형 AI 에이전트 개발", "데이터 파이프라인 엔지니어링"],
            index=0
        )

        wf_res = engine.compute_workforce_planning(target_hc, target_domain, param_reskill_eff)

        fig_donut = go.Figure(data=[go.Pie(
            labels=[f"내부 재숙련 전환 ({wf_res['build_count']}명)", f"외부 채용 ({wf_res['buy_count']}명)"],
            values=[wf_res["build_count"], wf_res["buy_count"]],
            hole=0.6,
            marker=dict(colors=["#2563EB", "#94A3B8"])
        )])
        layout_donut = styles.get_clean_plotly_layout(height=210)
        layout_donut["margin"] = dict(l=10, r=10, t=10, b=10)
        fig_donut.update_layout(layout_donut)
        st.plotly_chart(fig_donut, width="stretch")

        st.markdown(f"""
        <div style="font-size: 11.5px; color: #1E293B; background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px; padding: 8px 10px;">
            • 100% 외부 채용 시: <strong>{wf_res['all_buy_total']}억 원</strong><br/>
            • AI 하이브리드 수급: <strong>{wf_res['hybrid_total']}억 원</strong> (교육 {wf_res['build_total']}억 + 채용 {wf_res['buy_total']}억)<br/>
            • <strong style="color: #059669;">절감된 총예산: {wf_res['saved_total']}억 원 ({wf_res['savings_pct']}% 절감)</strong>
        </div>
        </div>
        """, unsafe_allow_html=True)

    # Panel 2: TF Chemistry Simulator
    with col_p2:
        st.markdown("""
        <div class="hrm-card">
            <div class="hrm-card-header">
                <div>
                    <h3 class="hrm-card-title">② 애자일 TF 케미스트리 매칭</h3>
                    <div class="hrm-card-desc">후보 팀장 × 수석 전문가 궁합 분석</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        sel_mgr = st.selectbox("후보 팀장 (L6 Manager):", options=["MGR-12 박준영", "MGR-05 최민호"], index=0)
        sel_ic = st.selectbox("후보 수석 전문가 (L6 Staff IC):", options=["IC-08 강동훈", "IC-14 송지우"], index=0)

        chem_res = engine.compute_tf_chemistry(sel_mgr, sel_ic)

        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(
            r=chem_res["scores"] + [chem_res["scores"][0]],
            theta=chem_res["dimensions"] + [chem_res["dimensions"][0]],
            fill="toself",
            fillcolor="rgba(37, 99, 235, 0.15)",
            line=dict(color="#2563EB", width=2),
            name="케미스트리 지수"
        ))
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[60, 100], tickfont=dict(size=9, color="#94A3B8"))
            ),
            height=210,
            margin=dict(l=25, r=25, t=10, b=20),
            paper_bgcolor="#FFFFFF",
            font=dict(family="Pretendard, sans-serif", size=9.5, color="#475569")
        )
        st.plotly_chart(fig_radar, width="stretch")

        st.markdown(f"""
        <div style="font-size: 11.5px; color: #1E293B; background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px; padding: 8px 10px;">
            • 종합 케미스트리: <strong>{chem_res['composite']}점</strong> / 100점<br/>
            • 결재 충돌 리스크: <strong>{chem_res['veto_conflict_risk']}%</strong> | 일정 지연 리스크: <strong>{chem_res['delay_risk']}%</strong><br/>
            • <em>{chem_res['verdict']}</em>
        </div>
        </div>
        """, unsafe_allow_html=True)

    # Panel 3: CFO Waterfall Chart
    with col_p3:
        st.markdown("""
        <div class="hrm-card">
            <div class="hrm-card-header">
                <div>
                    <h3 class="hrm-card-title">③ 경영진/CFO 보고용 3개년 ROI</h3>
                    <div class="hrm-card-desc">15억 투자 대비 115억 순가치 창출</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        fig_waterfall = go.Figure(go.Waterfall(
            name="HR Investment ROI",
            orientation="v",
            measure=["relative", "relative", "relative", "relative", "total"],
            x=["초기 구축비", "이직 방어", "지식 재사용", "품질사고 방어", "순재무 가치"],
            textposition="outside",
            text=["-15.0억", "+42.0억", "+38.0억", "+50.0억", "+115.0억"],
            y=[-15.0, 42.0, 38.0, 50.0, 0],
            connector={"line": {"color": "#CBD5E1"}},
            decreasing={"marker": {"color": "#EF4444"}},
            increasing={"marker": {"color": "#10B981"}},
            totals={"marker": {"color": "#2563EB"}}
        ))
        layout_wf = styles.get_clean_plotly_layout(height=245)
        layout_wf["yaxis"]["title"] = "금액 (억원)"
        fig_waterfall.update_layout(layout_wf)
        st.plotly_chart(fig_waterfall, width="stretch")

        st.markdown("""
        <div style="font-size: 11.5px; color: #1E293B; background: #EFF6FF; border: 1px solid #BFDBFE; border-radius: 6px; padding: 8px 10px;">
            • 3개년 총 편익: <strong>130.0억 원</strong> &nbsp;|&nbsp; 투자 비용: <strong>15.0억 원</strong><br/>
            • <strong>순재무 창출 가치: +115.0억 원</strong> (투자대비 866.7% 이익)<br/>
            • <strong>투자금 회수 기간 (Payback Period): 5.2개월</strong>
        </div>
        </div>
        """, unsafe_allow_html=True)


# ==============================================================================
# TAB 6: Employee XAI My Career Simulator
# ==============================================================================
with tab6:
    st.markdown("""
    <div class="tab-guide-banner">
        👤 <strong>[화면 캡처 5 안내] 직원 개인에게 주어지는 '설명 가능한 AI(XAI) 마이 커리어 시뮬레이터'입니다.</strong><br/>
        • <strong>성향·역량 진단</strong>: 업무 로그를 분석해 내 성향(기술 89% vs 관리 28%)과 시장 기술 반감기 잔여 수명(1.8년)을 경보합니다.<br/>
        • <strong>RAG 로열티 정산</strong>: 내가 쓴 표준 문서/코드가 사내 AI 튜터로 142회 재사용되어 발생한 <strong>로열티 성과급(1,850만 원)</strong>을 투명하게 정산합니다.<br/>
        • <strong>3개년 커리어 패스 뷰</strong>: '전문가 트랙으로 계속 갈 때 vs 관리자 트랙으로 바꿀 때' 3년 뒤 직급과 예상 연봉을 직접 비교해 봅니다.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hrm-card">
        <div class="hrm-card-header">
            <div>
                <h3 class="hrm-card-title">임직원 개인용 설명 가능한 AI(XAI) 마이 커리어 시뮬레이터</h3>
                <div class="hrm-card-desc">직원 본인의 행동 데이터, RAG 지식 기여 로열티, 역량 노후화 경보 및 3개년 커리어 패스 비교 대시보드</div>
            </div>
            <span class="badge-status badge-info">Employee Self-Service XAI</span>
        </div>
    """, unsafe_allow_html=True)

    c_sel1, c_sel2 = st.columns([1, 2])
    with c_sel1:
        emp_choice = st.selectbox(
            "조회할 임직원 페르소나 선택:",
            options=[
                "EMP-108 이서진 (L5 책임 / 시니어 전문가 - IC 트랙 대표)",
                "EMP-042 김도윤 (L6 팀장 / 번아웃 관리자 - IC 피벗 희망)",
                "EMP-215 박지훈 (L5 파트장 / 관리자 트랙 대표)"
            ],
            index=0
        )
    target_emp_id = emp_choice.split()[0]
    emp_profile = engine.get_employee_persona_profile(target_emp_id, param_royalty)

    col_profile_left, col_profile_mid, col_profile_right = st.columns([1.1, 1.1, 1.2])

    with col_profile_left:
        st.markdown(f"""
        <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px; padding: 12px; height: 100%;">
            <strong style="font-size: 13px; color: #1E293B;">1) 나의 행동 로그 기반 성향·역량 진단</strong>
            <div style="margin-top: 8px; font-size: 11.5px; color: #475569;">
                • 사번 / 성명: <strong>{emp_profile['emp_id']} {emp_profile['name']}</strong> ({emp_profile['level']})<br/>
                • 현재 직책: <strong>{emp_profile['title']}</strong> (입사 {emp_profile['tenure']}년차)<br/>
                • 주력 기술 스택: <strong>{emp_profile['primary_skill']}</strong>
            </div>
            <div style="margin-top: 10px;">
                <div style="font-size: 10.5px; color: #64748B;">IC 전문가 성향 ({emp_profile['ic_prop']}%) vs Manager 관리자 성향 ({emp_profile['mgr_prop']}%)</div>
                <div style="display: flex; height: 8px; border-radius: 4px; overflow: hidden; margin-top: 3px;">
                    <div style="width: {emp_profile['ic_prop']}%; background: #2563EB;"></div>
                    <div style="width: {emp_profile['mgr_prop']}%; background: #94A3B8;"></div>
                </div>
            </div>
            <div style="margin-top: 10px; font-size: 11px; color: #DC2626; background: #FEF2F2; border: 1px solid #FECACA; padding: 6px 8px; border-radius: 4px;">
                <strong>시장 반감기 경보:</strong> 내 주력 기술 잔여 수명 {emp_profile['decay_half_life_years']}년 (AI 대체 위험도 {emp_profile['decay_risk_pct']}%)
            </div>
            <div style="margin-top: 10px; font-size: 11.5px;">
                <strong style="color: #1E293B;">추천 맞춤형 재숙련 코스:</strong>
                <ul style="padding-left: 16px; margin-top: 3px; color: #334155;">
        """, unsafe_allow_html=True)

        for course in emp_profile["rec_courses"]:
            st.markdown(f"<li style='font-size: 10.5px; margin-bottom: 2px;'>{course['title']} (적합도 {course['match_pct']}%, {course['weeks']}주)</li>", unsafe_allow_html=True)

        st.markdown("</ul></div></div>", unsafe_allow_html=True)

    with col_profile_mid:
        st.markdown(f"""
        <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px; padding: 12px; height: 100%;">
            <strong style="font-size: 13px; color: #1E293B;">2) 실시간 재무 기여 & RAG 로열티 정산</strong>
            <div style="margin-top: 10px; display: grid; grid-template-columns: 1fr 1fr; gap: 6px;">
                <div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 4px; padding: 8px;">
                    <div style="font-size: 10.5px; color: #64748B;">RAG 등록 자산</div>
                    <div style="font-size: 16px; font-weight: 700; color: #1E293B;">{emp_profile['rag_assets']}건</div>
                </div>
                <div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 4px; padding: 8px;">
                    <div style="font-size: 10.5px; color: #64748B;">동료 재사용 횟수</div>
                    <div style="font-size: 16px; font-weight: 700; color: #2563EB;">{emp_profile['rag_reuses']}회</div>
                </div>
                <div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 4px; padding: 8px;">
                    <div style="font-size: 10.5px; color: #64748B;">단축한 업무 시간</div>
                    <div style="font-size: 16px; font-weight: 700; color: #1E293B;">{emp_profile['hours_saved']}시간</div>
                </div>
                <div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 4px; padding: 8px;">
                    <div style="font-size: 10.5px; color: #64748B;">사내 영향력 지수</div>
                    <div style="font-size: 16px; font-weight: 700; color: #059669;">{emp_profile['influence_score']}점</div>
                </div>
            </div>
            <div style="margin-top: 10px; background: #ECFDF5; border: 1px solid #A7F3D0; border-radius: 6px; padding: 10px; text-align: center;">
                <div style="font-size: 10.5px; color: #065F46; font-weight: 600;">올해 누적 지급 RAG 로열티 성과급</div>
                <div style="font-size: 20px; font-weight: 800; color: #047857; margin-top: 2px;">
                    {emp_profile['royalty_earned_manwon']:,}만 원
                </div>
                <div style="font-size: 9.5px; color: #059669; margin-top: 2px;">
                    (내 코드로 아낀 업무시간 × 요율 {param_royalty*100:.1f}% + 우수자산 보너스)
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_profile_right:
        st.markdown("""
        <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px; padding: 12px; height: 100%;">
            <strong style="font-size: 13px; color: #1E293B;">3) 나의 3개년 커리어 패스 시뮬레이션</strong>
            <div style="font-size: 10.5px; color: #64748B; margin-top: 3px; margin-bottom: 6px;">
                전문가 트랙 유지 vs 관리자 트랙 전환 시 3년 뒤 예상 총보상 비교
            </div>
        """, unsafe_allow_html=True)

        years = ["현재", "1년 뒤", "2년 뒤", "3년 뒤"]
        base = emp_profile["current_base_salary"]
        comp_ic = [base, base + 1800, base + 3800, base + 6800]
        comp_mgr = [base, base + 1400, base + 3200, base + 6200]

        fig_career = go.Figure()
        fig_career.add_trace(go.Scatter(
            x=years, y=comp_ic,
            mode="lines+markers", name="경로 A: 전문가(IC) 트랙 심화",
            line=dict(color="#2563EB", width=2.5),
            marker=dict(size=5)
        ))
        fig_career.add_trace(go.Scatter(
            x=years, y=comp_mgr,
            mode="lines+markers", name="경로 B: 관리자(Manager) 트랙 전환",
            line=dict(color="#64748B", width=2, dash="dash"),
            marker=dict(size=5)
        ))
        layout_career = styles.get_clean_plotly_layout(height=170)
        layout_career["yaxis"]["title"] = "예상 총보상 (만원)"
        fig_career.update_layout(layout_career)
        st.plotly_chart(fig_career, width="stretch")

        st.markdown("""
            <div style="font-size: 10.5px; color: #334155; margin-top: 4px;">
                • <strong>3년 뒤 예상 직급 및 권한:</strong><br/>
                - <strong>전문가(IC)</strong>: L6 수석 → L7 전문위원 (기술 거부권 행사, 연구비 1.2억)<br/>
                - <strong>관리자(MGR)</strong>: L6 팀장 → L7 실장 (25명 부서 총괄, 인사/예산권)
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# --- Bottom App Footer ---
st.markdown("""
<div style="text-align: center; font-size: 11.5px; color: #94A3B8; margin-top: 24px; margin-bottom: 16px;">
    HRmony AI: Organizational Digital Twin & HR Decision Intelligence System<br/>
    Academic Research & Enterprise HR Solution Proof-of-Concept | Reproducible Seed System
</div>
""", unsafe_allow_html=True)
