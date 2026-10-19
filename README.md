<!-- ═══════════════════════════════════════════════════════════════ -->
<!--   PROFILE README  ·  save as  Bhavesh-girase/README.md          -->
<!--   (repo name must match your username: Bhavesh-girase/Bhavesh-girase) -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=220&section=header&text=Bhavesh%20Girase&fontSize=58&fontColor=ffffff&animation=fadeIn&fontAlignY=36&desc=AI%20%C2%B7%20Machine%20Learning%20%C2%B7%20Full-Stack%20Engineering&descSize=18&descAlignY=58" width="100%" alt="Bhavesh Girase banner"/>

<a href="https://github.com/Bhavesh-girase">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=20&duration=3200&pause=900&color=3FB6D8&center=true&vCenter=true&width=700&lines=Building+AI+systems+that+actually+ship;Real-time+backends+%7C+RAG+pipelines+%7C+ML+in+production;Privacy-first+%C2%B7+Measured+%C2%B7+Reproducible;Hackathon+builder+%E2%80%94+SIH+2026+finalist+projects" alt="Typing SVG" />
</a>

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)

![Profile Views](https://komarev.com/ghpvc/?username=Bhavesh-girase&label=Profile%20Views&color=2c5364&style=flat-square)
![Repos](https://img.shields.io/badge/Public%20Repos-12-203a43?style=flat-square&logo=github)
![Focus](https://img.shields.io/badge/Focus-Applied%20AI%20%26%20Systems-0f2027?style=flat-square)

</div>

---

## 👨‍💻 About Me

I build **end-to-end intelligent systems**: from training a model to wrapping it in an API, shipping a polished UI, and load-testing the result. My projects share one habit: **claims backed by numbers**: benchmarks, load tests, and reproducible results rather than buzzwords.

| | |
|---|---|
| 🔭 **Currently exploring** | Repository-aware RAG, on-device ML, privacy-preserving AI agents |
| ⚙️ **Strong suit** | Taking ML from notebook → containerized API → deployed web app |
| 🏁 **Hackathons** | Smart India Hackathon 2026 (two problem statements, incl. ISRO PS26171) |
| 🧪 **Engineering style** | Atomic operations, formal verification, honest documentation |
| 🤝 **Open to** | Internships, collaborations, hackathon teams, open-source |

---

## 🏆 Featured Projects

### 🧾 [SpecSure](https://github.com/Bhavesh-girase/SpecsSure): *Tender Intelligence & Standards Compliance*
> **"Compile tenders like code. Prove compliance like math."** · Smart India Hackathon 2026 · PS SIH26108 · Team CodeNova

Treats government procurement tenders as **source code**: parses them into an AST, lints them with **38 rules** (SARIF 2.1.0 export), and uses the **Z3 SMT solver** to *prove* contradictory clauses with minimal unsatisfiable cores. It resolves Indian Standards as of the tender date and tracks corrigenda git-style. The LLM is optional and never decides, so every finding comes from the parser, rule engine, solver, or knowledge base.

`29,875 standards in KB` · `~15 ms mean compile` · `87.5% top-1 / 100% top-3 retrieval` · `60+ API endpoints` · `50 passing tests`
**Stack:** Python · Next.js · Z3 · Docker · MCP

---

### 🛡️ [Privacy Vision Agent](https://github.com/Bhavesh-girase/Privacy-Vision-Agent): *On-Device Visual Perception for Private Browser Automation*
> **"The AI never sees your data. It doesn't need to."** · SIH 2026 · ISRO · PS26171

A Manifest V3 Chrome extension that lets vision-language models navigate the web while PII is detected and redacted **entirely in your browser**. It combines regex with Luhn/Verhoeff checksums, ONNX NER, and YuNet face detection. A **Merkle-tree cryptographic proof** makes each redaction independently verifiable, and a 4-position **Privacy Dial** lets you choose how much to share.

`100% F1 on sensitive-data detection` · `38 PII fixtures · 14 countries · 0 false positives` · `52/52 hybrid-debate tests`
**Stack:** JavaScript · ONNX Runtime (WASM) · WebLLM (Qwen2.5) · Express · Chrome MV3

---

### 🤖 [AI PR Reviewer](https://github.com/Bhavesh-girase/ai-pr-reviewer) · [🌐 Live](https://aiprreviewer.vercel.app)
> *Repository-aware AI code reviews for GitHub Pull Requests*

A multi-tenant review platform that goes beyond the diff. **Hybrid RAG** (BM25 + vector search) feeds a **cross-encoder reranker** (`ms-marco-MiniLM-L-6-v2`), and **Gemini** generates the review. It includes GitHub integration, webhook-driven incremental indexing, a Monaco diff workspace, and review analytics.
**Stack:** React · TypeScript · Vite · FastAPI · LangChain · ChromaDB · Supabase · Docker · AWS EC2 · Vercel

---

### ⚡ [BidRush](https://github.com/Bhavesh-girase/BidRush): *Real-Time Auction Platform with Zero Race Conditions*

Redis **Lua scripts** make bid validation atomic. **RabbitMQ** offloads email and DB sync, and **Socket.io** pushes live updates. It also has a Stripe wallet and payments flow, an admin dashboard, and cron-driven auction lifecycles.

> 🎯 **k6 "Sniper" test: 500 users, same auction, same millisecond → 1 winner, 499 correctly rejected, 0 deadlocks, 0 inconsistencies, avg < 5 ms.**

**Stack:** React 19 · Node.js · PostgreSQL · Redis · RabbitMQ · Socket.io · Stripe · Cloudinary

---

## 🧠 Machine Learning & MLOps

| Project | What it does | Highlights | Links |
|:--|:--|:--|:--:|
| 🛡️ **fraud-mlops-api** | Real-time fraud detection inference service | CatBoost · **ROC-AUC ≈ 0.977** · precision 0.93 / recall 0.81 · tuned threshold 0.25 · FastAPI + Docker · Locust load-tested (~156 ms avg, ~31.8 req/s) | [Repo](https://github.com/Bhavesh-girase/fraud-mlops-api) |
| 🎧 **Speech Emotion Recognition** | Detects emotion from uploaded or live-mic audio | CNN + LSTM · trained on RAVDESS, CREMA-D, IEMOCAP · majority-vote utterance prediction · timeline & distribution views | [Backend](https://github.com/Bhavesh-girase/ser-backend) · [Frontend](https://github.com/Bhavesh-girase/ser-frontend) · [🌐 Live](https://ser-frontend-gamma.vercel.app) |
| ☀️ **SUNWISE** | Weekly solar AC-power & DC-current forecasting | Live geolocation + map input · prediction graphs · CSV/PDF export · green-impact estimate | [App](https://github.com/Bhavesh-girase/ML-HACKATHON-) · [🌐 Live](https://ml-hackathon-olive.vercel.app) · [Model](https://github.com/Bhavesh-girase/-SUNWISE-ML-MODEL) |

---

## 💬 More Builds

- 💬 **[Real-Time-Chat-App](https://github.com/Bhavesh-girase/Real-Time-Chat-App)**: a real-time chat application · [🌐 Live](https://chat-backend-eight-vert.vercel.app)
- 🔍 **[pr-review-test](https://github.com/Bhavesh-girase/pr-review-test)**: a sandbox for testing automated PR review

---

## 🧰 Tech Arsenal

<div align="center">

| Domain | Tools |
|:--|:--|
| **Languages** | ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square) ![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?logo=typescript&logoColor=white&style=flat-square) ![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?logo=javascript&logoColor=black&style=flat-square) |
| **ML / AI** | ![TensorFlow](https://img.shields.io/badge/-TensorFlow-FF6F00?logo=tensorflow&logoColor=white&style=flat-square) ![CatBoost](https://img.shields.io/badge/-CatBoost-FFCC00?style=flat-square) ![scikit-learn](https://img.shields.io/badge/-scikit--learn-F7931E?logo=scikitlearn&logoColor=white&style=flat-square) ![LangChain](https://img.shields.io/badge/-LangChain-1C3C3C?style=flat-square) ![Gemini](https://img.shields.io/badge/-Gemini-8E75B2?logo=googlegemini&logoColor=white&style=flat-square) ![ONNX](https://img.shields.io/badge/-ONNX-005CED?style=flat-square) ![ChromaDB](https://img.shields.io/badge/-ChromaDB-FF6446?style=flat-square) |
| **Frontend** | ![React](https://img.shields.io/badge/-React-61DAFB?logo=react&logoColor=black&style=flat-square) ![Next.js](https://img.shields.io/badge/-Next.js-000000?logo=nextdotjs&logoColor=white&style=flat-square) ![Vite](https://img.shields.io/badge/-Vite-646CFF?logo=vite&logoColor=white&style=flat-square) ![Tailwind](https://img.shields.io/badge/-Tailwind-06B6D4?logo=tailwindcss&logoColor=white&style=flat-square) |
| **Backend** | ![FastAPI](https://img.shields.io/badge/-FastAPI-009688?logo=fastapi&logoColor=white&style=flat-square) ![Node.js](https://img.shields.io/badge/-Node.js-339933?logo=nodedotjs&logoColor=white&style=flat-square) ![Express](https://img.shields.io/badge/-Express-000000?logo=express&logoColor=white&style=flat-square) ![Socket.io](https://img.shields.io/badge/-Socket.io-010101?logo=socketdotio&logoColor=white&style=flat-square) |
| **Data & Infra** | ![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-4169E1?logo=postgresql&logoColor=white&style=flat-square) ![Redis](https://img.shields.io/badge/-Redis-DC382D?logo=redis&logoColor=white&style=flat-square) ![RabbitMQ](https://img.shields.io/badge/-RabbitMQ-FF6600?logo=rabbitmq&logoColor=white&style=flat-square) ![Supabase](https://img.shields.io/badge/-Supabase-3FCF8E?logo=supabase&logoColor=white&style=flat-square) ![Docker](https://img.shields.io/badge/-Docker-2496ED?logo=docker&logoColor=white&style=flat-square) ![AWS](https://img.shields.io/badge/-AWS%20EC2-FF9900?logo=amazonec2&logoColor=white&style=flat-square) ![Vercel](https://img.shields.io/badge/-Vercel-000000?logo=vercel&logoColor=white&style=flat-square) |
| **Testing & Perf** | ![k6](https://img.shields.io/badge/-k6-7D64FF?logo=k6&logoColor=white&style=flat-square) ![Locust](https://img.shields.io/badge/-Locust-3F9E3F?style=flat-square) |

</div>

---

## 🏗️ How I Build

```mermaid
flowchart LR
    A[💡 Problem] --> B[🔬 Model / Algorithm]
    B --> C[⚙️ API & Services]
    C --> D[🖥️ Polished UI]
    D --> E[🐳 Containerize & Deploy]
    E --> F[📊 Load-test & Benchmark]
    F -->|measure, then claim| A
```

**Principles I follow**
- 📏 **Measure before you claim**: every headline number in my repos comes from a benchmark, a load test, or a test suite.
- 🔒 **Correctness by construction**: atomic Lua scripts, SMT proofs, and cryptographic redaction proofs instead of "trust me".
- 🔁 **Reproducible by default**: Docker, documented quick-starts, and benchmark scripts anyone can re-run.

---

## 📊 GitHub Stats

<div align="center">

<img height="170" src="https://github-readme-stats.vercel.app/api?username=Bhavesh-girase&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0f2027" alt="GitHub stats" />
<img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Bhavesh-girase&layout=compact&theme=tokyonight&hide_border=true&bg_color=0f2027" alt="Top languages" />

<img src="https://github-readme-streak-stats.herokuapp.com/?user=Bhavesh-girase&theme=tokyonight&hide_border=true&background=0f2027" alt="GitHub streak" />

<img src="https://github-profile-trophy.vercel.app/?username=Bhavesh-girase&theme=nord&no-frame=true&no-bg=true&margin-w=8&row=1&column=7" alt="Trophies" />

</div>

---

## 🤝 Let's Connect

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-Bhavesh--girase-181717?style=for-the-badge&logo=github)](https://github.com/Bhavesh-girase)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/YOUR-LINKEDIN-ID)
[![Email](https://img.shields.io/badge/Email-Say%20Hello-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:YOUR-EMAIL@example.com)

*Open to collaborations on applied AI, real-time systems, and hackathon teams.*

<br/>

> *"Compile it, prove it, benchmark it, ship it."*

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2c5364,50:203a43,100:0f2027&height=120&section=footer" width="100%" alt="footer"/>

</div>
