<div align="center">

<img src="assets/header.svg" width="100%" alt="Santiago Martín-Laborda: I build AI systems that run real businesses"/>

<br/>

<a href="https://kalu.lat"><img src="https://img.shields.io/badge/kalu.lat-live-22D3EE?style=for-the-badge&labelColor=0A0F1F" alt="kalu.lat"/></a>
<a href="https://www.linkedin.com/in/santiago-mart%C3%ADn-laborda-rodriguez-b522aa239/"><img src="https://img.shields.io/badge/LinkedIn-connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0A0F1F" alt="LinkedIn"/></a>
<a href="mailto:sannymanichi@gmail.com"><img src="https://img.shields.io/badge/Email-say%20hi-E3B341?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0A0F1F" alt="Email"/></a>
<img src="https://komarev.com/ghpvc/?username=santiagomlr&label=profile%20views&color=22D3EE&style=for-the-badge&labelColor=0A0F1F" alt="profile views"/>

<br/><br/>

<img src="assets/title-about.svg" width="100%" alt="About me"/>

<img src="assets/terminal.svg" width="100%" alt="santiago@brain ./profile --summary"/>

</div>

I'm a finance grad from **Tec de Monterrey** who ended up writing software because the spreadsheets stopped being enough. My day job is **Continuous Improvement at Grupo Senda**, a large Mexican transportation group, where I turn messy operations (fleet, treasury, payroll, maintenance) into AI-powered tools people actually use. On nights and weekends I'm building **[kalu](https://kalu.lat)**, which already has paying customers.

My rule of thumb: **if a task repeats, automate it. If it matters, measure it.**

<div align="center">

<img src="assets/title-build.svg" width="100%" alt="What I build"/>

<a href="https://kalu.lat"><img src="assets/card-kalu.svg" width="49%" alt="kalu"/></a>
<img src="assets/card-brain.svg" width="49%" alt="Brain OS"/>
<img src="assets/card-council.svg" width="49%" alt="Brain Council"/>
<img src="assets/card-atlas.svg" width="49%" alt="Atlas"/>
<img src="assets/card-flowsense.svg" width="49%" alt="FlowSense"/>
<img src="assets/card-sendastack.svg" width="49%" alt="SendaStack"/>

<img src="assets/title-brain.svg" width="100%" alt="How my brain works"/>

</div>

My most personal project is a **second brain that runs itself**. Every chat, meeting recording, email and Teams thread flows into a structured Obsidian wiki. Agents on an always-on home server keep it up to date, answer questions from my phone, schedule my calendar and run a council of 24 AI advisors when I have a hard call to make.

```mermaid
flowchart LR
    subgraph IN["📥 Sources"]
        WA["WhatsApp"]
        PL["Meeting recordings"]
        EM["Gmail · Outlook"]
        TM["Teams"]
    end
    subgraph CORE["🧠 Brain OS · home server"]
        RAW[("raw/")]
        ING["Ingest agents<br/>triage + extraction"]
        WIKI[("Wiki<br/>580+ pages")]
        IDX["Semantic index<br/>+ knowledge graph"]
    end
    subgraph OUT["⚡ Actions"]
        CAL["Calendar events"]
        TASK["Tasks"]
        CHAT["Brain chat app"]
        COUNCIL["24-agent council"]
    end
    WA & PL & EM & TM --> RAW --> ING --> WIKI --> IDX
    IDX --> CHAT & COUNCIL
    ING --> CAL & TASK
    classDef src fill:#0E1530,stroke:#22D3EE,color:#E2E8F0
    classDef core fill:#111933,stroke:#E3B341,color:#FDE68A
    classDef out fill:#0E1530,stroke:#A78BFA,color:#E2E8F0
    class WA,PL,EM,TM src
    class RAW,ING,WIKI,IDX core
    class CAL,TASK,CHAT,COUNCIL out
```

<div align="center">

<img src="assets/title-stack.svg" width="100%" alt="Toolkit"/>

<img src="https://skillicons.dev/icons?i=ts,react,vite,tailwind,nodejs,python,supabase,postgres&theme=dark" alt="TypeScript, React, Vite, Tailwind, Node.js, Python, Supabase, Postgres"/>
<br/>
<img src="https://skillicons.dev/icons?i=vercel,git,github,githubactions,obsidian,figma,vscode,linux&theme=dark" alt="Vercel, Git, GitHub, GitHub Actions, Obsidian, Figma, VS Code, Linux"/>

<br/><br/>

<img src="https://img.shields.io/badge/Claude%20%2B%20Claude%20Code-D97757?style=flat-square&logo=anthropic&logoColor=white" alt="Claude"/>
<img src="https://img.shields.io/badge/Multi--agent%20systems-0E1530?style=flat-square&logo=probot&logoColor=22D3EE" alt="Multi-agent systems"/>
<img src="https://img.shields.io/badge/Perplexity%20Sonar-1FB8CD?style=flat-square&logo=perplexity&logoColor=white" alt="Perplexity"/>
<img src="https://img.shields.io/badge/JD%20Edwards%20ERP-C74634?style=flat-square&logo=oracle&logoColor=white" alt="JD Edwards"/>
<img src="https://img.shields.io/badge/SQL%20Server-CC2927?style=flat-square&logo=microsoftsqlserver&logoColor=white" alt="SQL Server"/>
<img src="https://img.shields.io/badge/Stripe-635BFF?style=flat-square&logo=stripe&logoColor=white" alt="Stripe"/>
<img src="https://img.shields.io/badge/Financial%20modeling-E3B341?style=flat-square&logo=googlesheets&logoColor=0A0F1F" alt="Financial modeling"/>

<img src="assets/title-stats.svg" width="100%" alt="By the numbers"/>

<img src="https://raw.githubusercontent.com/santiagomlr/santiagomlr/output/stats.svg" width="100%" alt="Contribution dashboard"/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/santiagomlr/santiagomlr/output/github-contribution-grid-snake-dark.svg"/>
  <img width="100%" alt="Contribution snake" src="https://raw.githubusercontent.com/santiagomlr/santiagomlr/output/github-contribution-grid-snake.svg"/>
</picture>

<img src="assets/title-contact.svg" width="100%" alt="Let's talk"/>

<b>Building something in B2B data, AI agents or operations? I'd love to hear about it.</b>

<a href="https://www.linkedin.com/in/santiago-mart%C3%ADn-laborda-rodriguez-b522aa239/"><img src="https://img.shields.io/badge/LinkedIn-Santiago%20Mart%C3%ADn--Laborda-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
<a href="https://kalu.lat"><img src="https://img.shields.io/badge/Try-kalu.lat-22D3EE?style=for-the-badge&labelColor=0A0F1F" alt="kalu"/></a>

<sub>Graphics are hand-built SVGs in this repo; stats refresh automatically every 6 hours via GitHub Actions.</sub>

</div>
