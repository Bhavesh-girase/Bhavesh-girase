"""Generates every SVG in ../assets. Run from repo root:  python3 tools/generate_assets.py"""
import os
from xml.sax.saxutils import escape as E
try:
    from PIL import ImageFont
    _F=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",13)
    def tw(t,size=13): return _F.getlength(t)*size/13*0.96
except Exception:
    def tw(t,size=13): return len(t)*size*0.55

SANS="'Segoe UI', -apple-system, 'Helvetica Neue', Arial, sans-serif"
MONO="'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace"
CY,VI,AM,GR,PK="#38bdf8","#818cf8","#fbbf24","#34d399","#f472b6"
INK,MUTE,DIM="#f1f5f9","#a9b6cf","#64748b"
PANEL,LINE="#0b1324","#1e2d4d"
OUT=os.path.join(os.path.dirname(__file__),"..","assets"); os.makedirs(OUT,exist_ok=True)

def save(name,w,h,body,defs=""):
    open(os.path.join(OUT,name+".svg"),"w",encoding="utf-8").write(
      f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img">\n<defs>{defs}</defs>\n{body}\n</svg>\n')
def lg(id,c1,c2,c3=None,x2="100%",y2="0%"):
    s=f'<stop offset="0" stop-color="{c1}"/>'+(f'<stop offset=".5" stop-color="{c2}"/><stop offset="1" stop-color="{c3}"/>' if c3 else f'<stop offset="1" stop-color="{c2}"/>')
    return f'<linearGradient id="{id}" x1="0%" y1="0%" x2="{x2}" y2="{y2}">{s}</linearGradient>'
def rg(id,c,op): return f'<radialGradient id="{id}"><stop offset="0" stop-color="{c}" stop-opacity="{op}"/><stop offset="1" stop-color="{c}" stop-opacity="0"/></radialGradient>'

# ───────── HERO ─────────
def hero():
    W,H=880,390
    layers=[("AGENTS","retrieve · reason · act",VI),("COMPLIANCE","rules · proofs · audit trail",AM),("PRIVACY","on-device · redact · verify",GR),("SCALE","async · atomic · load-tested",CY)]
    y0,step,rail=78,76,520; ys=[y0+i*step+29 for i in range(4)]
    top,bot=52,352
    L=""
    for i,(t,s,c) in enumerate(layers):
        y=y0+i*step; f=(ys[i]-top)/(bot-top)
        kt=f"0;{max(f-.08,0):.3f};{f:.3f};{min(f+.08,1):.3f};1"
        L+=f'''<g><rect x="540" y="{y}" width="300" height="58" rx="12" fill="#0d1730" stroke="{LINE}"/>
<rect x="540" y="{y}" width="5" height="58" rx="2.5" fill="{c}"/>
<text x="562" y="{y+25}" font-family="{MONO}" font-size="13" font-weight="700" letter-spacing="1.2" fill="{c}">{t}</text>
<text x="562" y="{y+44}" font-family="{SANS}" font-size="13" fill="{MUTE}">{E(s)}</text>
<line x1="{rail}" y1="{ys[i]}" x2="540" y2="{ys[i]}" stroke="{c}" stroke-opacity=".5" stroke-dasharray="3 4"/>
<rect x="540" y="{y}" width="300" height="58" rx="12" fill="{c}" fill-opacity=".14" stroke="{c}" stroke-width="1.6" opacity="0"><animate attributeName="opacity" values="0;0;1;0;0" keyTimes="{kt}" dur="6s" repeatCount="indefinite"/></rect></g>'''
    defs=f'''{lg("bg","#05080f","#0b1226","#150f2a","100%","100%")}{rg("g1",VI,.42)}{rg("g2",CY,.30)}
<linearGradient id="nm" gradientUnits="userSpaceOnUse" x1="44" y1="0" x2="470" y2="0"><stop offset="0" stop-color="{CY}"/><stop offset=".55" stop-color="{VI}"/><stop offset="1" stop-color="{PK}"/></linearGradient>
<pattern id="gd" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#16223d" stroke-width="1"/></pattern>
<radialGradient id="fd"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#000"/></radialGradient><mask id="mk"><rect width="{W}" height="{H}" fill="url(#fd)"/></mask>{lg("ed",CY,VI,PK)}'''
    body=f'''<rect width="{W}" height="{H}" rx="22" fill="url(#bg)"/>
<rect width="{W}" height="{H}" fill="url(#gd)" mask="url(#mk)"/>
<circle cx="150" cy="90" r="260" fill="url(#g1)"/><circle cx="720" cy="330" r="280" fill="url(#g2)"/>
<text x="44" y="86" font-family="{MONO}" font-size="13" letter-spacing="2.2" fill="{CY}">// AI · SYSTEMS · SECURITY</text>
<text x="42" y="150" font-family="{SANS}" font-size="52" font-weight="800" fill="url(#nm)">Bhavesh Girase</text>
<text x="44" y="196" font-family="{SANS}" font-size="20" fill="#cbd5e1">I build AI systems that are</text>
<text x="44" y="226" font-family="{SANS}" font-size="20" font-weight="700"><tspan fill="{CY}">scalable</tspan><tspan fill="#475569"> · </tspan><tspan fill="{VI}">agentic</tspan><tspan fill="#475569"> · </tspan><tspan fill="{AM}">verifiable</tspan><tspan fill="#475569"> · </tspan><tspan fill="{GR}">private</tspan></text>
<g transform="translate(44,262)"><rect width="318" height="36" rx="18" fill="#0a1a1a" stroke="#14532d"/><circle cx="20" cy="18" r="5" fill="{GR}"/><circle cx="20" cy="18" r="5" fill="none" stroke="{GR}"><animate attributeName="r" values="5;14;5" dur="2.4s" repeatCount="indefinite"/><animate attributeName="opacity" values=".8;0;.8" dur="2.4s" repeatCount="indefinite"/></circle><text x="38" y="23" font-family="{SANS}" font-size="14" font-weight="600" fill="#a7f3d0">Open to internships &amp; opportunities</text></g>
<text x="44" y="338" font-family="{MONO}" font-size="12.5" fill="{DIM}">Smart India Hackathon 2026 · ISRO problem statement</text>
<text x="44" y="358" font-family="{MONO}" font-size="12.5" fill="{DIM}">Full-stack · ML · LLM agents · backend infrastructure</text>
<text x="{rail}" y="38" text-anchor="middle" font-family="{MONO}" font-size="11" letter-spacing="1.5" fill="{DIM}">REQUEST</text>
<line x1="{rail}" y1="{top}" x2="{rail}" y2="{bot}" stroke="{LINE}" stroke-width="2"/>
<path d="M{rail-5},{bot-6} L{rail},{bot+2} L{rail+5},{bot-6}" fill="none" stroke="{LINE}" stroke-width="2"/>
<text x="{rail}" y="376" text-anchor="middle" font-family="{MONO}" font-size="11" letter-spacing="1.5" fill="{DIM}">TRUSTED OUTPUT</text>
{L}
<circle r="6" fill="#fff"><animateMotion dur="6s" repeatCount="indefinite" path="M{rail},{top} V{bot}"/></circle>
<circle r="14" fill="#fff" opacity=".18"><animateMotion dur="6s" repeatCount="indefinite" path="M{rail},{top} V{bot}"/></circle>
<rect x="0" y="{H-3}" width="{W}" height="3" fill="url(#ed)" opacity=".9"/>'''
    save("hero",W,H,body,defs)

# ───────── SECTION HEADER ─────────
def header(name,eyebrow,title,c):
    W,H=880,86
    body=f'''<text x="2" y="26" font-family="{MONO}" font-size="12.5" letter-spacing="2.4" fill="{c}">{E(eyebrow)}</text>
<text x="0" y="62" font-family="{SANS}" font-size="30" font-weight="800" fill="{INK}">{E(title)}</text>
<rect x="0" y="76" width="{W}" height="1.5" fill="{LINE}"/><rect x="0" y="75" width="64" height="3.5" rx="1.75" fill="{c}"/>'''
    save(name,W,H,body)

# ───────── PILLAR CARDS ─────────
ICONS={
 "scale":'<g fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="5" r="2.6"/><circle cx="5" cy="19" r="2.6"/><circle cx="19" cy="19" r="2.6"/><path d="M12 7.6V12M12 12L6.2 16.8M12 12l5.8 4.8"/></g>',
 "agent":'<g fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="5" cy="12" r="2.6"/><circle cx="19" cy="5" r="2.6"/><circle cx="19" cy="19" r="2.6"/><path d="M7.4 11L16.6 6M7.4 13l9.2 5"/><path d="M12 12h1.5"/></g>',
 "shield":'<g fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.8l7.5 3v5.6c0 4.8-3.2 8.6-7.5 10-4.3-1.4-7.5-5.2-7.5-10V5.8z"/><path d="M8.6 12.2l2.6 2.6 4.4-5"/></g>',
 "lock":'<g fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4.5" y="10.5" width="15" height="10.5" rx="2.6"/><path d="M8 10.5V8a4 4 0 0 1 8 0v2.5"/><circle cx="12" cy="15.8" r="1.4" fill="{c}"/></g>'}
def pillar(name,num,title,desc,bullets,c,icon):
    W,H=432,268
    b="".join(f'<rect x="28" y="{196+i*24-8}" width="7" height="7" rx="2" fill="{c}"/><text x="46" y="{196+i*24}" font-family="{SANS}" font-size="13.5" fill="#dbe4f3">{E(t)}</text>' for i,t in enumerate(bullets))
    d="".join(f'<text x="28" y="{112+i*21}" font-family="{SANS}" font-size="14" fill="{MUTE}">{E(t)}</text>' for i,t in enumerate(desc))
    defs=rg("gl",c,.30)+f'<clipPath id="cp"><rect width="{W}" height="{H}" rx="18"/></clipPath>'
    body=f'''<g clip-path="url(#cp)"><rect width="{W}" height="{H}" fill="{PANEL}"/><circle cx="{W-20}" cy="10" r="200" fill="url(#gl)"/><rect width="{W}" height="3" fill="{c}" opacity=".9"/></g>
<rect x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="17.5" fill="none" stroke="{LINE}" stroke-width="1.5"/>
<rect x="28" y="26" width="48" height="48" rx="14" fill="{c}" fill-opacity=".12" stroke="{c}" stroke-opacity=".4"/>
<g transform="translate(40,38) scale(1)">{ICONS[icon].format(c=c)}</g>
<text x="92" y="44" font-family="{MONO}" font-size="11.5" letter-spacing="2" fill="{c}">FOCUS {num}</text>
<text x="92" y="68" font-family="{SANS}" font-size="21" font-weight="800" fill="{INK}">{E(title)}</text>
{d}
<line x1="28" y1="150" x2="{W-28}" y2="150" stroke="{LINE}"/>
<text x="28" y="174" font-family="{MONO}" font-size="11" letter-spacing="2" fill="{DIM}">IN PRACTICE</text>{b}'''
    save(name,W,H,body,defs)

# ───────── PRINCIPLES ─────────
def principles():
    W,H=880,206
    cols=[("01",["Deterministic first,","LLM second."],["Solvers and rules make the call;","models draft, explain and assist,","but never get the final word."],AM),
          ("02",["Privacy by","architecture."],["Handle sensitive data where it lives.","Make leaks structurally impossible,","not just against the rules."],GR),
          ("03",["Measure,","then claim."],["Every headline number comes from a","benchmark, load test or test suite,","so anyone can re-run it."],CY)]
    cw=W/3; body=f'<rect width="{W}" height="{H}" rx="18" fill="{PANEL}"/><rect x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="17.5" fill="none" stroke="{LINE}" stroke-width="1.5"/>'
    for i,(n,t,d,c) in enumerate(cols):
        x=cw*i+30
        if i: body+=f'<line x1="{cw*i}" y1="28" x2="{cw*i}" y2="{H-28}" stroke="{LINE}"/>'
        body+=f'<text x="{x}" y="42" font-family="{MONO}" font-size="11.5" letter-spacing="2" fill="{c}">PRINCIPLE {n}</text>'
        body+="".join(f'<text x="{x}" y="{72+k*25}" font-family="{SANS}" font-size="20" font-weight="800" fill="{INK}">{E(l)}</text>' for k,l in enumerate(t))
        body+=f'<rect x="{x}" y="{128}" width="28" height="3" rx="1.5" fill="{c}"/>'
        body+="".join(f'<text x="{x}" y="{152+k*18}" font-family="{SANS}" font-size="13" fill="{MUTE}">{E(l)}</text>' for k,l in enumerate(d))
    save("principles",W,H,body)

# ───────── CAPABILITY MAP ─────────
def skills():
    W=832; LX=206; maxx=W
    rows=[("Agentic AI & LLMs",VI,["LangChain","Gemini API","Hybrid RAG","BM25 + vectors","Cross-encoder reranking","ChromaDB","WebLLM · Qwen2.5","MCP","Prompt & context design"],["LangGraph","LLM evals","Prompt-injection defence"]),
          ("ML & MLOps",CY,["Python","TensorFlow · Keras","CatBoost","scikit-learn","ONNX Runtime","pandas · NumPy","Librosa","OpenCV","Model serving (FastAPI)"],["MLflow","Drift monitoring","Quantisation"]),
          ("Backend & Scale",GR,["Node.js","Express","FastAPI","PostgreSQL","Redis · Lua","RabbitMQ","Socket.io","REST design","Stripe","k6 · Locust"],["Kafka","Kubernetes","OpenTelemetry"]),
          ("Security · Privacy · Compliance",AM,["PII detection (regex · NER)","Redaction & Merkle proofs","Z3 SMT solver","SARIF linting","JWT · HTTP-only auth","Supabase Auth","Pydantic · Zod validation","W3C Verifiable Credentials"],["OWASP LLM Top 10","Differential privacy","Threat modelling"]),
          ("Frontend & Product",PK,["React","Next.js","TypeScript","JavaScript","Vite","Tailwind CSS","Monaco editor","Chrome extensions (MV3)"],[]),
          ("Cloud & Delivery",CY,["Docker","AWS EC2","Vercel","Render","Git · GitHub API","Webhooks"],["Terraform","CI/CD pipelines"])]
    y=64; body=""
    # legend
    body+=f'<circle cx="{W-262}" cy="22" r="5" fill="{CY}"/><text x="{W-250}" y="26.5" font-family="{SANS}" font-size="13" fill="{MUTE}">used in my projects</text>'
    body+=f'<circle cx="{W-110}" cy="22" r="4.5" fill="none" stroke="{MUTE}" stroke-width="1.5"/><text x="{W-98}" y="26.5" font-family="{SANS}" font-size="13" fill="{MUTE}">exploring</text>'
    for ri,(label,c,have,exp) in enumerate(rows):
        x=LX; cy=y; chips=""
        items=[(t,True) for t in have]+[(t,False) for t in exp]
        for t,on in items:
            w=tw(t)+34
            if x+w>maxx: x=LX; cy+=40
            if on: chips+=f'<g transform="translate({x:.0f},{cy})"><rect width="{w:.0f}" height="32" rx="16" fill="#0f1a33" stroke="{LINE}"/><circle cx="16" cy="16" r="4.5" fill="{c}"/><text x="28" y="21" font-family="{SANS}" font-size="13" fill="#e2e8f0">{E(t)}</text></g>'
            else: chips+=f'<g transform="translate({x:.0f},{cy})"><rect x=".75" y=".75" width="{w-1.5:.0f}" height="30.5" rx="15.25" fill="none" stroke="{c}" stroke-opacity=".55" stroke-dasharray="4 4"/><circle cx="16" cy="16" r="4" fill="none" stroke="{c}" stroke-width="1.5"/><text x="28" y="21" font-family="{SANS}" font-size="13" fill="{MUTE}">{E(t)}</text></g>'
            x+=w+8
        rh=cy+32-y
        lab=label if len(label)<24 else None
        if lab: body+=f'<text x="0" y="{y+21}" font-family="{SANS}" font-size="15" font-weight="700" fill="{INK}">{E(lab)}</text>'
        else:
            a,b=label.split(" · ",1)[0],label.split(" · ",1)[1]
            body+=f'<text x="0" y="{y+14}" font-family="{SANS}" font-size="15" font-weight="700" fill="{INK}">Security · Privacy</text><text x="0" y="{y+33}" font-family="{SANS}" font-size="15" font-weight="700" fill="{INK}">&amp; Compliance</text>'
        body+=f'<rect x="0" y="{y+(36 if lab else 42)}" width="26" height="3" rx="1.5" fill="{c}"/>'
        body+=chips
        y+=rh+16
        if ri<len(rows)-1: body+=f'<line x1="0" y1="{y-8}" x2="{W}" y2="{y-8}" stroke="{LINE}" stroke-opacity=".6"/>'
    H=y-4
    body=f'<rect width="880" height="{H+48}" rx="18" fill="{PANEL}"/><rect x=".75" y=".75" width="878.5" height="{H+46.5}" rx="17.5" fill="none" stroke="{LINE}" stroke-width="1.5"/><g transform="translate(24,24)">'+body+'</g>'
    save("skills",880,H+48,body)

# ───────── OPPORTUNITIES ─────────
def open_to():
    W,H=880,338
    roles=["AI / ML Engineer Intern","LLM & Agent Systems Intern","Backend / Platform Engineer Intern","AI Security, Privacy & Compliance"]
    r="".join(f'<g transform="translate(566,{84+i*38})"><rect width="284" height="32" rx="10" fill="#0f1a33" stroke="{LINE}"/><path d="M14 16h10M20 11l5 5-5 5" fill="none" stroke="{GR}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><text x="38" y="21" font-family="{SANS}" font-size="13.5" fill="#e2e8f0">{E(t)}</text></g>' for i,t in enumerate(roles))
    bring=[("Ships end-to-end","model → API → UI → deploy",CY),("Thinks in guarantees","proofs, atomicity, privacy",AM),("Proves with numbers","benchmarks over buzzwords",GR)]
    bx="".join(f'<g transform="translate({28+i*284},256)"><rect width="268" height="64" rx="12" fill="#0f1a33" stroke="{LINE}"/><rect x="0" y="14" width="4" height="36" rx="2" fill="{c}"/><text x="20" y="28" font-family="{SANS}" font-size="14.5" font-weight="700" fill="{INK}">{E(t)}</text><text x="20" y="48" font-family="{MONO}" font-size="12" fill="{MUTE}">{E(s)}</text></g>' for i,(t,s,c) in enumerate(bring))
    defs=lg("bg","#08111f","#0d1a30","#10142b","100%","100%")+rg("gg",GR,.22)
    body=f'''<rect width="{W}" height="{H}" rx="20" fill="url(#bg)"/><circle cx="120" cy="30" r="260" fill="url(#gg)"/>
<rect x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="19.5" fill="none" stroke="{LINE}" stroke-width="1.5"/>
<circle cx="40" cy="40" r="5.5" fill="{GR}"/><circle cx="40" cy="40" r="5.5" fill="none" stroke="{GR}"><animate attributeName="r" values="5.5;15;5.5" dur="2.4s" repeatCount="indefinite"/><animate attributeName="opacity" values=".8;0;.8" dur="2.4s" repeatCount="indefinite"/></circle>
<text x="58" y="45" font-family="{MONO}" font-size="12.5" letter-spacing="2.2" fill="{GR}">AVAILABLE · OPEN TO OPPORTUNITIES</text>
<text x="28" y="98" font-family="{SANS}" font-size="27" font-weight="800" fill="{INK}">Looking for internships</text>
<text x="28" y="134" font-family="{SANS}" font-size="27" font-weight="800" fill="{INK}">where AI meets real engineering.</text>
<text x="28" y="168" font-family="{SANS}" font-size="14.5" fill="{MUTE}">I want to join a team that builds, ships and measures: production AI,</text>
<text x="28" y="190" font-family="{SANS}" font-size="14.5" fill="{MUTE}">agentic systems, and infrastructure people can trust.</text>
<text x="566" y="70" font-family="{MONO}" font-size="11.5" letter-spacing="2" fill="{DIM}">TARGET ROLES</text>{r}{bx}
<line x1="544" y1="64" x2="544" y2="232" stroke="{LINE}"/>'''
    save("open",W,H,body,defs)

def footer():
    W,H=880,120
    body=f'''<rect width="{W}" height="{H}" rx="18" fill="{PANEL}"/><rect x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="17.5" fill="none" stroke="{LINE}" stroke-width="1.5"/>
<text x="{W/2}" y="52" text-anchor="middle" font-family="{SANS}" font-size="21" font-style="italic" fill="#e2e8f0">“Compile it. Prove it. Benchmark it. Ship it.”</text>
<text x="{W/2}" y="82" text-anchor="middle" font-family="{MONO}" font-size="12" letter-spacing="3" fill="{DIM}">BHAVESH GIRASE</text>
<rect x="0" y="{H-4}" width="{W}" height="4" rx="2" fill="url(#ed)"/><rect x="0" y="{H-4}" width="120" height="4" rx="2" fill="#fff" opacity=".7"><animate attributeName="x" values="-120;{W}" dur="5s" repeatCount="indefinite"/></rect>'''
    save("footer",W,H,body,lg("ed",CY,VI,PK))

hero()
header("h-focus","01 · FOCUS AREAS","What I build",CY)
header("h-think","02 · PRINCIPLES","How I think",AM)
header("h-skills","03 · CAPABILITY MAP","Skills & stack",VI)
header("h-open","04 · OPPORTUNITIES","Let's work together",GR)
header("h-signal","05 · SIGNAL","GitHub activity",PK)
pillar("p-scale","01","Scalable Systems",["Backends that stay correct under pressure:","concurrent, event-driven and load-tested."],
 ["Atomic hot paths with Redis Lua scripting","Event-driven: RabbitMQ workers, WebSockets","Load-tested with k6 & Locust, shipped in Docker"],CY,"scale")
pillar("p-agent","02","Agentic Workflows",["LLM agents that retrieve, reason and act, with","guardrails around every consequential step."],
 ["Hybrid RAG: BM25 + vectors + cross-encoder rerank","Multi-agent debate & tool-using browser agents","On-device + cloud LLMs: WebLLM, Gemini, MCP"],VI,"agent")
pillar("p-comply","03","Compliance & Verification",["Turning rules into something a machine can prove,","not something a model merely has an opinion on."],
 ["Z3 SMT proofs with minimal unsatisfiable cores","Rule engines, SARIF linting, hash-chained audits","Deterministic-first: LLMs assist, never decide"],AM,"shield")
pillar("p-privacy","04","Privacy & Security",["Privacy enforced by architecture: sensitive data","stays on the device, and you can verify it."],
 ["On-device PII detection & pixel-level redaction","Merkle-tree proofs that redaction really happened","JWT / HTTP-only auth, encrypted local stores"],GR,"lock")
principles();skills();open_to();footer()
