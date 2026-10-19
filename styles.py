"""
HRmony AI - Enterprise Design System and Styling Tokens
Benchmark: Modern People Analytics Platforms (Visier, Workday Peakon, Lattice, Mercer)
Theme: Academic & Enterprise White/Slate Theme with High Contrast Visuals
"""

ENTERPRISE_CSS = """
<style>
/* Main typography and container spacing */
@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');

html, body, [class*="css"] {
    font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
    color: #0F172A;
}

/* Remove default extra padding in Streamlit */
.block-container {
    padding-top: 1.2rem !important;
    padding-bottom: 2.0rem !important;
    max-width: 98% !important;
}

/* Header bar styling */
.hrm-header-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 8px;
    padding: 14px 22px;
    margin-bottom: 14px;
    box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04);
}

.hrm-title-area {
    display: flex;
    flex-direction: column;
}

.hrm-title {
    font-size: 21px;
    font-weight: 700;
    color: #0F172A;
    letter-spacing: -0.02em;
    margin: 0;
    display: flex;
    align-items: center;
    gap: 8px;
}

.hrm-title-highlight {
    color: #2563EB;
}

.hrm-subtitle {
    font-size: 13px;
    color: #64748B;
    margin-top: 3px;
    margin-bottom: 0;
}

.hrm-header-meta {
    display: flex;
    gap: 10px;
}

.hrm-meta-badge {
    display: inline-flex;
    align-items: center;
    padding: 4px 10px;
    border-radius: 6px;
    font-size: 11px;
    font-weight: 600;
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    color: #334155;
}

.hrm-meta-badge.active {
    background: #EFF6FF;
    border-color: #BFDBFE;
    color: #1D4ED8;
}

/* Executive Overview Hero Banner (Fixed height, no bottom whitespace) */
.hrm-hero-banner {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 8px;
    padding: 14px 18px;
    margin-bottom: 14px;
    box-shadow: 0 1px 2px rgba(15, 23, 42, 0.03);
}

.hrm-hero-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    margin-top: 10px;
}

.hrm-hero-card {
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 6px;
    padding: 12px 14px;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
}

.hrm-hero-card.problem {
    border-left: 3px solid #EF4444;
}

.hrm-hero-card.solution {
    border-left: 3px solid #2563EB;
}

.hrm-hero-card.simulator {
    border-left: 3px solid #10B981;
}

.hrm-hero-card-title {
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 5px;
    display: flex;
    align-items: center;
    gap: 6px;
}

.hrm-hero-card-desc {
    font-size: 11.5px;
    color: #475569;
    line-height: 1.5;
    margin: 0;
}

/* General Card Containers */
.hrm-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 8px;
    padding: 16px 20px;
    margin-bottom: 14px;
    box-shadow: 0 1px 3px rgba(15, 23, 42, 0.03);
}

.hrm-card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #F1F5F9;
    padding-bottom: 10px;
    margin-bottom: 12px;
}

.hrm-card-title {
    font-size: 14px;
    font-weight: 700;
    color: #1E293B;
    margin: 0;
    letter-spacing: -0.01em;
}

.hrm-card-desc {
    font-size: 11.5px;
    color: #64748B;
    margin-top: 2px;
}

/* Metric Display Cards */
.hrm-kpi-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin-bottom: 14px;
}

.hrm-kpi-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 8px;
    padding: 14px 18px;
    box-shadow: 0 1px 2px rgba(15, 23, 42, 0.03);
    position: relative;
}

.hrm-kpi-label {
    font-size: 11.5px;
    font-weight: 600;
    color: #64748B;
    margin-bottom: 4px;
}

.hrm-kpi-value-row {
    display: flex;
    align-items: baseline;
    gap: 8px;
}

.hrm-kpi-value-treatment {
    font-size: 23px;
    font-weight: 800;
    color: #1D4ED8;
    letter-spacing: -0.02em;
}

.hrm-kpi-value-control {
    font-size: 13px;
    font-weight: 500;
    color: #94A3B8;
}

.hrm-kpi-delta {
    display: inline-flex;
    align-items: center;
    font-size: 11px;
    font-weight: 600;
    padding: 2px 6px;
    border-radius: 4px;
    margin-top: 5px;
}

.hrm-kpi-delta.positive {
    background: #ECFDF5;
    color: #047857;
    border: 1px solid #A7F3D0;
}

.hrm-kpi-delta.negative {
    background: #FEF2F2;
    color: #B91C1C;
    border: 1px solid #FECACA;
}

/* Redesigned Presentation-Ready Segmented Tabs */
div[data-baseweb="tab-list"], div[data-testid="stTabs"] > div {
    background-color: #F8FAFC !important;
    border: 1px solid #E2E8F0 !important;
    border-radius: 8px !important;
    padding: 4px !important;
    gap: 4px !important;
    margin-bottom: 16px !important;
}

div[data-baseweb="tab"], button[data-baseweb="tab"] {
    height: 40px !important;
    border-radius: 6px !important;
    font-weight: 600 !important;
    font-size: 12.5px !important;
    color: #475569 !important;
    padding: 0 14px !important;
    border: none !important;
    background: transparent !important;
    transition: all 0.15s ease-in-out !important;
}

div[data-baseweb="tab"]:hover, button[data-baseweb="tab"]:hover {
    background-color: #EDE9FE !important;
    color: #1E293B !important;
}

div[data-baseweb="tab"][aria-selected="true"], button[data-baseweb="tab"][aria-selected="true"] {
    background-color: #2563EB !important;
    color: #FFFFFF !important;
    box-shadow: 0 1px 3px rgba(37, 99, 235, 0.25) !important;
}

/* Sidebar styling and Compact Parameter Help */
section[data-testid="stSidebar"] {
    background-color: #FFFFFF;
    border-right: 1px solid #E2E8F0;
    padding-top: 1rem;
}

section[data-testid="stSidebar"] h1, 
section[data-testid="stSidebar"] h2, 
section[data-testid="stSidebar"] h3 {
    font-size: 13.5px !important;
    font-weight: 700;
    color: #1E293B;
    letter-spacing: -0.01em;
}

/* Compact Parameter Guide Card (Sidebar) */
.param-help {
    background: #F8FAFC;
    border-left: 3px solid #2563EB;
    padding: 5px 8px;
    margin-top: -8px;
    margin-bottom: 12px;
    border-radius: 0 4px 4px 0;
    font-size: 11px;
    line-height: 1.4;
}

.param-meaning {
    color: #334155;
    margin-bottom: 2px;
}

.param-impact {
    color: #0369A1;
    font-weight: 600;
}

/* Status Badges */
.badge-status {
    padding: 3px 8px;
    border-radius: 4px;
    font-size: 11px;
    font-weight: 600;
    display: inline-block;
}
.badge-success { background: #ECFDF5; color: #047857; border: 1px solid #A7F3D0; }
.badge-warning { background: #FFFBEB; color: #B45309; border: 1px solid #FDE68A; }
.badge-danger  { background: #FEF2F2; color: #B91C1C; border: 1px solid #FECACA; }
.badge-info    { background: #EFF6FF; color: #1D4ED8; border: 1px solid #BFDBFE; }
.badge-neutral { background: #F1F5F9; color: #475569; border: 1px solid #CBD5E1; }

/* Custom table styling */
.hrm-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 12.5px;
    margin-top: 6px;
}
.hrm-table th {
    background-color: #F8FAFC;
    color: #475569;
    font-weight: 600;
    text-align: left;
    padding: 8px 12px;
    border-bottom: 2px solid #E2E8F0;
}
.hrm-table td {
    padding: 8px 12px;
    border-bottom: 1px solid #F1F5F9;
    color: #1E293B;
}
.hrm-table tr:hover {
    background-color: #F8FAFC;
}

/* Tab Banner Box */
.tab-guide-banner {
    background: #EFF6FF;
    border: 1px solid #BFDBFE;
    border-radius: 6px;
    padding: 10px 14px;
    margin-bottom: 12px;
    font-size: 12px;
    color: #1E40AF;
    line-height: 1.5;
}

/* Clean buttons */
.stButton > button {
    border-radius: 6px;
    font-weight: 600;
    font-size: 12.5px;
    border: 1px solid #CBD5E1;
    background-color: #FFFFFF;
    color: #1E293B;
    transition: all 0.15s ease;
}
.stButton > button:hover {
    border-color: #2563EB;
    color: #2563EB;
}
.stButton > button[kind="primary"] {
    background-color: #2563EB;
    color: #FFFFFF;
    border-color: #2563EB;
}
.stButton > button[kind="primary"]:hover {
    background-color: #1D4ED8;
    border-color: #1D4ED8;
}

/* Hide streamlit default branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

# Palette Constants for Plotly Charts
COLOR_CONTROL = "#EF4444"       # Clean Crimson Red for Control Group
COLOR_CONTROL_LIGHT = "#FCA5A5"
COLOR_TREATMENT = "#2563EB"     # Royal Cobalt Blue for Treatment Group
COLOR_TREATMENT_LIGHT = "#93C5FD"
COLOR_SUCCESS = "#10B981"       # Emerald for Defense / Retention
COLOR_WARNING = "#F59E0B"       # Amber for Warning / Mismatch
COLOR_SLATE_DARK = "#1E293B"    # Deep Slate
COLOR_SLATE_MUTED = "#64748B"   # Muted Slate
COLOR_GRID = "#F1F5F9"          # Light Slate Grid lines

def get_clean_plotly_layout(height=360, title=None):
    """Returns a standardized high-contrast enterprise Plotly layout dict."""
    return dict(
        height=height,
        title=dict(
            text=title or "",
            font=dict(family="Pretendard, sans-serif", size=13, color="#1E293B", weight=700),
            x=0.01,
            y=0.96
        ),
        margin=dict(l=40, r=20, t=42 if title else 20, b=36),
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        font=dict(family="Pretendard, sans-serif", size=11, color="#475569"),
        hoverlabel=dict(
            bgcolor="#1E293B",
            font_size=11,
            font_family="Pretendard, sans-serif",
            font_color="#FFFFFF"
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(size=10.5, color="#475569")
        ),
        xaxis=dict(
            gridcolor=COLOR_GRID,
            linecolor="#E2E8F0",
            zerolinecolor="#E2E8F0",
            tickfont=dict(size=10.5, color="#64748B")
        ),
        yaxis=dict(
            gridcolor=COLOR_GRID,
            linecolor="#E2E8F0",
            zerolinecolor="#E2E8F0",
            tickfont=dict(size=10.5, color="#64748B")
        )
    )
