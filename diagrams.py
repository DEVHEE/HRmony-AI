"""
HRmony AI - High-Resolution SVG Diagrams for Proposal Specification
[도식 1] 4단계 폐루프(Closed-Loop) 전체 아키텍처 로직맵
[도식 2] 멀티 에이전트 월 단위 상태 전이 및 의사결정 알고리즘 로직맵
Self-contained HTML documents for st.components.v1.html rendering
"""

def get_diagram_1_html():
    """Returns standalone HTML document containing SVG for [도식 1] 4단계 폐루프 전체 아키텍처."""
    return """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body {
    margin: 0; padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Pretendard", sans-serif;
    background: transparent;
    overflow-x: auto;
    overflow-y: hidden;
  }
  .diagram-container {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 8px;
    padding: 14px 18px;
    box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04);
    min-width: 1060px;
  }
</style>
</head>
<body>
<div class="diagram-container">
  <svg viewBox="0 0 1080 435" width="100%" height="435" xmlns="http://www.w3.org/2000/svg" style="font-family: inherit;">
    <defs>
      <!-- Shadow -->
      <filter id="card-shadow" x="-3%" y="-4%" width="106%" height="110%" filterUnits="userSpaceOnUse">
        <feDropShadow dx="0" dy="1.5" stdDeviation="2.5" flood-color="#0F172A" flood-opacity="0.05"/>
      </filter>
      <!-- Arrow Markers -->
      <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#2563EB"/>
      </marker>
      <marker id="loop-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#10B981"/>
      </marker>
    </defs>

    <!-- Header Titles -->
    <text x="10" y="22" font-size="14" font-weight="700" fill="#0F172A">&lt;도식 1&gt; AI 기반 동적 이중경력경로 및 시뮬레이션 검증 4단계 폐루프(Closed-Loop) 전체 아키텍처</text>
    <text x="10" y="40" font-size="11" fill="#64748B">업무 로그 진단(모듈 1) → 동적 재숙련·RAG(모듈 2) → 4대 HR 코어(모듈 3) → 가상조직 시뮬레이션·전략 환류(모듈 4)의 선순환</text>

    <!-- MODULE 1 CARD -->
    <g transform="translate(10, 58)" filter="url(#card-shadow)">
      <rect width="240" height="295" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
      <rect width="240" height="34" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
      <rect y="22" width="240" height="12" fill="#F8FAFC"/>
      <text x="12" y="22" font-size="12" font-weight="700" fill="#1E293B">[설계 모듈 1] 진단·경로 설계</text>
      <rect x="178" y="7" width="50" height="20" rx="4" fill="#EFF6FF" stroke="#BFDBFE"/>
      <text x="186" y="21" font-size="10" font-weight="600" fill="#1D4ED8">INPUT</text>

      <g transform="translate(10, 46)">
        <rect width="220" height="50" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
        <text x="10" y="19" font-size="11" font-weight="700" fill="#2563EB">1) 행동 로그 기반 성향 분석</text>
        <text x="10" y="36" font-size="10" fill="#64748B">Git/Wiki(IC) vs Jira/Slack(MGR)</text>
      </g>
      <g transform="translate(10, 106)">
        <rect width="220" height="50" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
        <text x="10" y="19" font-size="11" font-weight="700" fill="#0F172A">2) 시장 연동 마이크로 KPI</text>
        <text x="10" y="36" font-size="10" fill="#64748B">외부 JD 크롤링 및 기술 스택 대조</text>
      </g>
      <g transform="translate(10, 166)">
        <rect width="220" height="50" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
        <text x="10" y="19" font-size="11" font-weight="700" fill="#0F172A">3) 기술 권위(Authority) 매칭</text>
        <text x="10" y="36" font-size="10" fill="#64748B">직책 대신 영향력 지표(Influence) 환산</text>
      </g>
      <g transform="translate(10, 226)">
        <rect width="220" height="50" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
        <text x="10" y="19" font-size="11" font-weight="700" fill="#0F172A">4) 양방향 커리어 피벗(Pivot)</text>
        <text x="10" y="36" font-size="10" fill="#64748B">스킬 갭 진단 & 단기 TF 테스트베드</text>
      </g>
    </g>

    <!-- Arrow 1 -> 2 -->
    <path d="M 255 205 L 280 205" fill="none" stroke="#2563EB" stroke-width="2.5" marker-end="url(#arrow)"/>

    <!-- MODULE 2 CARD -->
    <g transform="translate(285, 58)" filter="url(#card-shadow)">
      <rect width="240" height="295" rx="8" fill="#FFFFFF" stroke="#93C5FD" stroke-width="1.8"/>
      <rect width="240" height="34" rx="8" fill="#EFF6FF" stroke="#93C5FD" stroke-width="1.8"/>
      <rect y="22" width="240" height="12" fill="#EFF6FF"/>
      <text x="12" y="22" font-size="12" font-weight="700" fill="#1D4ED8">[설계 모듈 2] 맞춤형 학습·LXP</text>
      <rect x="172" y="7" width="56" height="20" rx="4" fill="#DBEAFE" stroke="#93C5FD"/>
      <text x="178" y="21" font-size="10" font-weight="600" fill="#1E40AF">RESKILL</text>

      <g transform="translate(10, 46)">
        <rect width="220" height="50" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
        <text x="10" y="19" font-size="11" font-weight="700" fill="#2563EB">1) 트랙 연동 맞춤형 온보딩</text>
        <text x="10" y="36" font-size="10" fill="#64748B">IC 심화 R&D vs MGR 리더십 위임</text>
      </g>
      <g transform="translate(10, 106)">
        <rect width="220" height="50" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
        <text x="10" y="19" font-size="11" font-weight="700" fill="#0F172A">2) 동적 재숙련(Reskilling) 엔진</text>
        <text x="10" y="36" font-size="10" fill="#64748B">기술 반감기 경보 & 인접 역량 전이</text>
      </g>
      <g transform="translate(10, 166)">
        <rect width="220" height="50" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
        <text x="10" y="19" font-size="11" font-weight="700" fill="#0F172A">3) 브릿지 러닝(Bridge Learning)</text>
        <text x="10" y="36" font-size="10" fill="#64748B">AI 페르소나 코칭 & 테크 리프레시</text>
      </g>
      <g transform="translate(10, 226)">
        <rect width="220" height="50" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
        <text x="10" y="19" font-size="11" font-weight="700" fill="#0F172A">4) 노하우 RAG 자동 교재화</text>
        <text x="10" y="36" font-size="10" fill="#64748B">전문가 산출물 AI 튜터화 & 재사용 추적</text>
      </g>
    </g>

    <!-- Arrow 2 -> 3 -->
    <path d="M 530 205 L 555 205" fill="none" stroke="#2563EB" stroke-width="2.5" marker-end="url(#arrow)"/>

    <!-- MODULE 3 CARD -->
    <g transform="translate(560, 58)" filter="url(#card-shadow)">
      <rect width="240" height="295" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
      <rect width="240" height="34" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
      <rect y="22" width="240" height="12" fill="#F8FAFC"/>
      <text x="12" y="22" font-size="12" font-weight="700" fill="#1E293B">[설계 모듈 3] 4대 HR 코어</text>
      <rect x="178" y="7" width="50" height="20" rx="4" fill="#FEF3C7" stroke="#FCD34D"/>
      <text x="186" y="21" font-size="10" font-weight="600" fill="#92400E">CORE</text>

      <g transform="translate(10, 46)">
        <rect width="220" height="50" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
        <text x="10" y="19" font-size="11" font-weight="700" fill="#2563EB">1) [평가] 직무 성과 재무 환산</text>
        <text x="10" y="36" font-size="10" fill="#64748B">원가절감·손실방어·매출기여 단일화</text>
      </g>
      <g transform="translate(10, 106)">
        <rect width="220" height="50" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
        <text x="10" y="19" font-size="11" font-weight="700" fill="#0F172A">2) [매칭] L5~L8 통합 레벨링</text>
        <text x="10" y="36" font-size="10" fill="#64748B">IC(수석/위원) vs MGR(팀장/실장) 1:1</text>
      </g>
      <g transform="translate(10, 166)">
        <rect width="220" height="50" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
        <text x="10" y="19" font-size="11" font-weight="700" fill="#0F172A">3) [대우] 결재권 분리 & Veto</text>
        <text x="10" y="36" font-size="10" fill="#64748B">전문가 기술 승인권 및 거부권 보장</text>
      </g>
      <g transform="translate(10, 226)">
        <rect width="220" height="50" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
        <text x="10" y="19" font-size="11" font-weight="700" fill="#0F172A">4) [보상] 지식 로열티 & 육성급</text>
        <text x="10" y="36" font-size="10" fill="#64748B">RAG 재사용 절감액 % + 팀원성장 연동</text>
      </g>
    </g>

    <!-- Arrow 3 -> 4 -->
    <path d="M 805 205 L 830 205" fill="none" stroke="#2563EB" stroke-width="2.5" marker-end="url(#arrow)"/>

    <!-- MODULE 4 CARD -->
    <g transform="translate(835, 58)" filter="url(#card-shadow)">
      <rect width="235" height="295" rx="8" fill="#FFFFFF" stroke="#A7F3D0" stroke-width="1.8"/>
      <rect width="235" height="34" rx="8" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="1.8"/>
      <rect y="22" width="235" height="12" fill="#ECFDF5"/>
      <text x="12" y="22" font-size="12" font-weight="700" fill="#065F46">[설계 모듈 4] 시뮬레이션·환류</text>
      <rect x="172" y="7" width="50" height="20" rx="4" fill="#D1FAE5" stroke="#6EE7B7"/>
      <text x="180" y="21" font-size="10" font-weight="600" fill="#047857">TWIN</text>

      <g transform="translate(10, 46)">
        <rect width="215" height="50" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
        <text x="10" y="19" font-size="11" font-weight="700" fill="#047857">1) 가상 조직 A/B 시뮬레이션</text>
        <text x="10" y="36" font-size="10" fill="#64748B">N=500, t=60개월 가상조직 검증</text>
      </g>
      <g transform="translate(10, 106)">
        <rect width="215" height="50" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
        <text x="10" y="19" font-size="11" font-weight="700" fill="#0F172A">2) 5대 인사난제 정량검증</text>
        <text x="10" y="36" font-size="10" fill="#64748B">피터의 법칙, 반감기, 사일로 타파</text>
      </g>
      <g transform="translate(10, 166)">
        <rect width="215" height="50" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
        <text x="10" y="19" font-size="11" font-weight="700" fill="#0F172A">3) 선제적 핀셋 리텐션</text>
        <text x="10" y="36" font-size="10" fill="#64748B">Flight Risk 경보 & 맞춤형 오퍼</text>
      </g>
      <g transform="translate(10, 226)">
        <rect width="215" height="50" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
        <text x="10" y="19" font-size="11" font-weight="700" fill="#0F172A">4) Buy vs Build & TF 최적화</text>
        <text x="10" y="36" font-size="10" fill="#64748B">인력수급 황금비율 & 케미스트리</text>
      </g>
    </g>

    <!-- CLOSED LOOP FEEDBACK (Bottom Arrow) -->
    <path d="M 952 360 L 952 395 L 125 395 L 125 360" fill="none" stroke="#10B981" stroke-width="2.5" stroke-dasharray="6,4" marker-end="url(#loop-arrow)"/>
    <rect x="385" y="383" width="310" height="24" rx="12" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="1"/>
    <text x="400" y="399" font-size="11" font-weight="600" fill="#065F46">시뮬레이션 검증 및 현장 실측 데이터 피드백 루프 (Closed-Loop HR 환류)</text>
  </svg>
</div>
</body>
</html>
"""

def get_diagram_2_html():
    """Returns standalone HTML document containing SVG for [도식 2] 멀티 에이전트 월 단위 상태 전이 순서도."""
    return """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body {
    margin: 0; padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Pretendard", sans-serif;
    background: transparent;
    overflow-x: auto;
    overflow-y: hidden;
  }
  .diagram-container {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 8px;
    padding: 14px 18px;
    box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04);
    min-width: 1060px;
  }
</style>
</head>
<body>
<div class="diagram-container">
  <svg viewBox="0 0 1080 445" width="100%" height="445" xmlns="http://www.w3.org/2000/svg" style="font-family: inherit;">
    <defs>
      <filter id="node-shadow" x="-3%" y="-4%" width="106%" height="110%" filterUnits="userSpaceOnUse">
        <feDropShadow dx="0" dy="1.5" stdDeviation="2.5" flood-color="#0F172A" flood-opacity="0.05"/>
      </filter>
      <marker id="flow-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#2563EB"/>
      </marker>
      <marker id="branch-stay" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#10B981"/>
      </marker>
      <marker id="branch-pivot" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#6366F1"/>
      </marker>
      <marker id="branch-quit" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#EF4444"/>
      </marker>
    </defs>

    <!-- Header -->
    <text x="10" y="22" font-size="14" font-weight="700" fill="#0F172A">&lt;도식 2&gt; 멀티 에이전트(Multi-Agent) 타임스텝(월 단위) 상태 전이 및 의사결정 알고리즘 로직맵</text>
    <text x="10" y="40" font-size="11" fill="#64748B">개별 임직원 에이전트(i=1..500)가 매월(t=1..60) 경험하는 환경 충격, 제도적 상호작용 및 3대 행동 분기(Stay / Pivot / Attrition)</text>

    <!-- Step 1: Work & Shock -->
    <g transform="translate(10, 58)" filter="url(#node-shadow)">
      <rect width="240" height="175" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
      <rect width="240" height="28" rx="8" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1.5"/>
      <rect y="16" width="240" height="12" fill="#F1F5F9"/>
      <text x="10" y="19" font-size="12" font-weight="700" fill="#1E293B">Step 1. 월간 업무 수행 & 노후화 충격</text>
      
      <text x="10" y="48" font-size="11" font-weight="600" fill="#0F172A">사내 업무 로그 자동 축적</text>
      <text x="10" y="66" font-size="10" fill="#64748B">• Git 코드 커밋, Wiki 기술 표준화 문서</text>
      <text x="10" y="82" font-size="10" fill="#64748B">• Jira 병목 이슈 해결, Slack 조율 로그</text>
      
      <line x1="10" y1="98" x2="228" y2="98" stroke="#E2E8F0"/>
      <text x="10" y="116" font-size="11" font-weight="600" fill="#DC2626">외부 AI 기술 반감기 충격</text>
      <text x="10" y="134" font-size="10" fill="#64748B">• 연간 25% 가치 자연 노후화 발생</text>
      <text x="10" y="150" font-size="10" fill="#334155" font-family="monospace">ΔSkill = -λ · Skill(t-1)</text>
    </g>

    <!-- Arrow 1 -> 2 -->
    <path d="M 255 145 L 280 145" fill="none" stroke="#2563EB" stroke-width="2.5" marker-end="url(#flow-arrow)"/>

    <!-- Step 2: Track Fit -->
    <g transform="translate(285, 58)" filter="url(#node-shadow)">
      <rect width="240" height="175" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
      <rect width="240" height="28" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
      <rect y="16" width="240" height="12" fill="#F8FAFC"/>
      <text x="10" y="19" font-size="12" font-weight="700" fill="#1E293B">Step 2. 트랙 적합도 진단 & 분기</text>

      <rect x="10" y="38" width="220" height="58" rx="4" fill="#FEF2F2" stroke="#FECACA"/>
      <text x="14" y="54" font-size="10" font-weight="700" fill="#B91C1C">Control: 연차 승진 관행</text>
      <text x="14" y="70" font-size="9" fill="#7F1D1D">고연차 IC 강제 관리직 배치</text>
      <text x="14" y="84" font-size="9" fill="#991B1B">→ 피터의 법칙 부조화 & 마이크로매니징</text>

      <rect x="10" y="104" width="220" height="58" rx="4" fill="#EFF6FF" stroke="#BFDBFE"/>
      <text x="14" y="120" font-size="10" font-weight="700" fill="#1D4ED8">Treatment: AI 성향 진단</text>
      <text x="14" y="136" font-size="9" fill="#1E40AF">IC vs MGR 최적 경로 분기 추천</text>
      <text x="14" y="150" font-size="9" fill="#1E3A8A">L5~L8 수석/위원 기술 권위 매칭</text>
    </g>

    <!-- Arrow 2 -> 3 -->
    <path d="M 530 145 L 555 145" fill="none" stroke="#2563EB" stroke-width="2.5" marker-end="url(#flow-arrow)"/>

    <!-- Step 3: Reskill & RAG -->
    <g transform="translate(560, 58)" filter="url(#node-shadow)">
      <rect width="240" height="175" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
      <rect width="240" height="28" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
      <rect y="16" width="240" height="12" fill="#F8FAFC"/>
      <text x="10" y="19" font-size="12" font-weight="700" fill="#1E293B">Step 3. 재숙련 & RAG 학습 자산화</text>

      <rect x="10" y="38" width="220" height="58" rx="4" fill="#FEF2F2" stroke="#FECACA"/>
      <text x="14" y="54" font-size="10" font-weight="700" fill="#B91C1C">Control: 획일적 집체 교육</text>
      <text x="14" y="70" font-size="9" fill="#7F1D1D">기술 노후화 방치, 지식 독점</text>
      <text x="14" y="84" font-size="9" fill="#991B1B">→ 퇴사 시 기술 공백 5.8개월</text>

      <rect x="10" y="104" width="220" height="58" rx="4" fill="#EFF6FF" stroke="#BFDBFE"/>
      <text x="14" y="120" font-size="10" font-weight="700" fill="#1D4ED8">Treatment: 적시형 동적 재숙련</text>
      <text x="14" y="136" font-size="9" fill="#1E40AF">인접 역량 전이 효율 85% 유지</text>
      <text x="14" y="150" font-size="9" fill="#1E3A8A">사내 RAG 튜터화 (공백 1.4개월 단축)</text>
    </g>

    <!-- Arrow 3 -> 4 -->
    <path d="M 805 145 L 830 145" fill="none" stroke="#2563EB" stroke-width="2.5" marker-end="url(#flow-arrow)"/>

    <!-- Step 4: Finance & Rewards -->
    <g transform="translate(835, 58)" filter="url(#node-shadow)">
      <rect width="235" height="175" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
      <rect width="235" height="28" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
      <rect y="16" width="235" height="12" fill="#F8FAFC"/>
      <text x="10" y="19" font-size="12" font-weight="700" fill="#1E293B">Step 4. 재무 환산 & 보상 정산</text>

      <text x="10" y="48" font-size="11" font-weight="600" fill="#0F172A">성과 재무지표(억원) 환산</text>
      <text x="10" y="66" font-size="10" fill="#64748B">• IC: 원가절감 + 결함방어(Veto)</text>
      <text x="10" y="82" font-size="10" fill="#64748B">• MGR: 이직방어 + 일정준수</text>

      <line x1="10" y1="98" x2="223" y2="98" stroke="#E2E8F0"/>
      <text x="10" y="116" font-size="11" font-weight="600" fill="#2563EB">보상 자동 정산</text>
      <text x="10" y="134" font-size="10" fill="#64748B">• 통합 직급별 동일 기본급</text>
      <text x="10" y="150" font-size="10" fill="#64748B">• RAG 지식 재사용 로열티 (4%)</text>
    </g>

    <!-- Arrow to Step 5 -->
    <path d="M 952 238 L 952 260 L 125 260 L 125 275" fill="none" stroke="#2563EB" stroke-width="2.5" marker-end="url(#flow-arrow)"/>

    <!-- Step 5: Utility Calculation Bar -->
    <g transform="translate(10, 285)" filter="url(#node-shadow)">
      <rect width="1060" height="50" rx="8" fill="#F8FAFC" stroke="#2563EB" stroke-width="1.5"/>
      <text x="14" y="20" font-size="11" font-weight="700" fill="#1E293B">Step 5. 에이전트 유틸리티 만족도(S_t) 및 이탈 확률(Flight Risk) 동적 산출</text>
      <text x="14" y="38" font-size="10" fill="#475569">
        만족도: <tspan font-family="monospace" font-weight="600" fill="#2563EB">S(t) = w₁·Fit + w₂·Comp + w₃·Autonomy - w₄·DecayStress</tspan> &nbsp;|&nbsp; 
        외부 격차: <tspan font-family="monospace" font-weight="600" fill="#DC2626">G(t) = MarketWage - CurrentComp</tspan> &nbsp;|&nbsp; 
        이탈확률: <tspan font-family="monospace" font-weight="600" fill="#0F172A">P_quit = σ(α·(100 - S(t)) + β·G(t) + γ·StressDomino)</tspan>
      </text>
    </g>

    <!-- 3-Way Branching -->
    <!-- Branch A: Stay (Left) -->
    <path d="M 175 340 L 175 365" fill="none" stroke="#10B981" stroke-width="2.5" marker-end="url(#branch-stay)"/>
    <g transform="translate(10, 370)">
      <rect width="330" height="60" rx="6" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="1.5"/>
      <text x="12" y="20" font-size="11" font-weight="700" fill="#065F46">분기 A: 잔류 및 고몰입 (Stay & Engagement)</text>
      <text x="12" y="36" font-size="10" fill="#047857">조건: 만족도 S(t) ≥ 65점 &amp; 이탈확률 P_quit &lt; 0.25</text>
      <text x="12" y="50" font-size="10" fill="#064E3B">결과: L5~L8 지속 승격, 사내 RAG 자산화, 높은 재무기여</text>
    </g>

    <!-- Branch B: Pivot (Center) -->
    <path d="M 540 340 L 540 365" fill="none" stroke="#6366F1" stroke-width="2.5" marker-end="url(#branch-pivot)"/>
    <g transform="translate(360, 370)">
      <rect width="350" height="60" rx="6" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1.5"/>
      <text x="12" y="20" font-size="11" font-weight="700" fill="#4338CA">분기 B: 커리어 피벗 & 브릿지 러닝 (Career Pivot)</text>
      <text x="12" y="36" font-size="10" fill="#4F46E5">조건: 트랙 부조화 감지 (Treatment 그룹 한정 자동 제안)</text>
      <text x="12" y="50" font-size="10" fill="#312E81">결과: AI 페르소나 코칭/테크 리프레시 후 수평 이동 (이탈 차단)</text>
    </g>

    <!-- Branch C: Attrition (Right) -->
    <path d="M 900 340 L 900 365" fill="none" stroke="#EF4444" stroke-width="2.5" marker-end="url(#branch-quit)"/>
    <g transform="translate(735, 370)">
      <rect width="335" height="60" rx="6" fill="#FEF2F2" stroke="#FECACA" stroke-width="1.5"/>
      <text x="12" y="20" font-size="11" font-weight="700" fill="#B91C1C">분기 C: 퇴사 및 도미노 연쇄 이탈 (Attrition)</text>
      <text x="12" y="36" font-size="10" fill="#DC2626">조건: 만족도 S(t) &lt; 40점 &amp; 이탈확률 P_quit ≥ 0.70</text>
      <text x="12" y="50" font-size="10" fill="#7F1D1D">결과: 핵심인재 유출, 도미노 연쇄 이탈, 대규모 대체손실 발생</text>
    </g>
  </svg>
</div>
</body>
</html>
"""
