<!--
   ┌─────────────────────────────┐
   │  ((•))  ─────────  ((•))    │   si llegaste hasta aquí:
   │   side A · no rebobinar     │   hay una side B al final
   └─────────────────────────────┘
-->

<div align="center">

<img src="./assets/banner.svg" alt="Nakusu" width="100%" />

<br/>

<a href="https://instagram.com/n4kusu">
  <img src="https://img.shields.io/badge/Instagram-1C1F1C?style=for-the-badge&logo=instagram&logoColor=9B4A55&labelColor=1C1F1C" alt="Instagram"/>
</a>
<a href="https://github.com/Nakusuo?tab=repositories">
  <img src="https://img.shields.io/badge/Repos-1C1F1C?style=for-the-badge&logo=github&logoColor=C9C2B0&labelColor=1C1F1C" alt="Repos"/>
</a>
<img src="https://komarev.com/ghpvc/?username=Nakusuo&style=for-the-badge&color=4a5f3a&label=VISITAS" alt="visitas"/>
<img src="https://img.shields.io/github/followers/Nakusuo?style=for-the-badge&label=SEGUIDORES&color=5a2430&labelColor=1C1F1C" alt="seguidores"/>
<img src="https://img.shields.io/github/stars/Nakusuo?style=for-the-badge&label=ESTRELLAS&color=4a382c&labelColor=1C1F1C" alt="estrellas"/>
<img src="https://img.shields.io/badge/Lima-Per%C3%BA-1C1F1C?style=for-the-badge&logo=googlemaps&logoColor=A9856B&labelColor=1C1F1C" alt="Lima, Perú"/>

<br/>

<img src="https://readme-typing-svg.demolab.com?font=VT323&size=30&pause=1400&color=8FA36B&center=true&vCenter=true&width=560&lines=Estudiante+de+Ingenier%C3%ADa+de+Software;Frontend+en+React+%2B+TypeScript;Backend+en+Spring+Boot+y+FastAPI;Dise%C3%B1o%2C+arte+y+c%C3%B3digo+creativo" alt="typing"/>


<br/><br/>

<sub><code>TRACKLIST</code></sub>
<br/>
<a href="#-whoami"><img src="https://img.shields.io/badge/01-whoami-1C1F1C?style=flat-square&labelColor=42553a" alt="01 whoami"/></a>
<a href="#-en-qué-ando"><img src="https://img.shields.io/badge/02-proyectos-1C1F1C?style=flat-square&labelColor=5a2430" alt="02 proyectos"/></a>
<a href="#-stack"><img src="https://img.shields.io/badge/03-stack-1C1F1C?style=flat-square&labelColor=4a382c" alt="03 stack"/></a>
<a href="#-métricas"><img src="https://img.shields.io/badge/04-m%C3%A9tricas-1C1F1C?style=flat-square&labelColor=42553a" alt="04 métricas"/></a>
<a href="#-últimos-movimientos"><img src="https://img.shields.io/badge/05-actividad-1C1F1C?style=flat-square&labelColor=5a2430" alt="05 actividad"/></a>
<a href="#side-b"><img src="https://img.shields.io/badge/%E2%96%B8-side_B-1C1F1C?style=flat-square&labelColor=4a382c" alt="side B"/></a>

</div>

<a href="https://github.com/Nakusuo?tab=repositories"><img src="./assets/now-playing.svg" width="100%" alt="Reproduciendo: mi último movimiento en GitHub"/></a>

<img src="./assets/divider.svg" width="100%" alt=""/>

## `>` whoami

```ts
const nakusu = {
  rol:        "Estudiante de Ingeniería de Software · 3er año",
  ahora:      ["Huecko", "SafeZone", "Clínica Biométrica"],
  frontend:   ["React", "TypeScript", "Tailwind", "Vite"],
  backend:    ["Spring Boot", "FastAPI", "PostgreSQL"],
  tambien:    ["diseño", "ilustración", "3D", "edición"],
  filosofia:  "si se ve bien y además funciona, mejor",
};
```

Me muevo entre el diseño y el código: me importa tanto que la arquitectura tenga
sentido como que la interfaz se sienta bien de usar. Aquí subo proyectos de
universidad, prácticas y cosas que hago por curiosidad.


```console
$ git log --oneline --graph side-a
* a5f0e2c (HEAD -> side-a, tag: v0.5.0) feat(huecko): servicio de IA con Gemini + despliegue
* 7c41b9d (tag: v0.4.0) feat(huecko): panel de administración · salud · fallos · consola
* 3e9d1a7 feat(safezone): botón de pánico con GPS y alertas en tiempo real
* 91b27f4 feat(clinica): API de telemedicina con facial-login y Swagger
* 0c0ffee init: ingeniería de software ☕
```

<img src="./assets/divider.svg" width="100%" alt=""/>

## `>` en qué ando

<details open>
<summary><b>🗓️ &nbsp;Huecko</b> &nbsp;—&nbsp; coordinar planes entre amigos sin 40 mensajes de WhatsApp</summary>

<br/>

<a href="https://github.com/Nakusuo/huecko-frontend">
  <img src="./assets/huecko.svg" width="100%" alt="Huecko — heatmap de disponibilidad del grupo"/>
</a>

<img src="https://img.shields.io/badge/release-v0.5.0_%C2%B7_IA_y_despliegue-1C1F1C?style=flat-square&labelColor=42553a"/>
<img src="https://img.shields.io/badge/modos-conectado_%C2%B7_stub_%C2%B7_demo-1C1F1C?style=flat-square&labelColor=4a382c"/>
<img src="https://img.shields.io/badge/roles-USUARIO_%C2%B7_ADMIN-1C1F1C?style=flat-square&labelColor=5a2430"/>


Sistema completo en tres repos. Los usuarios registran su disponibilidad
(bloques recurrentes y puntuales), la app cruza horarios y propone ventanas
donde el grupo realmente coincide.

- **Heatmap semanal** de disponibilidad del grupo, con umbral configurable
- **Propuestas con votación**: 2–5 ventanas, confirmación, retrasos e imprevistos
- **Importación OCR** de horarios en borrador
- Modo demo sin backend + backend stub para desarrollo
- Contrato de API documentado entre front y Spring Boot

<img src="https://img.shields.io/badge/React-1C1F1C?style=flat-square&logo=react&logoColor=7A8F5C&labelColor=1C1F1C"/>
<img src="https://img.shields.io/badge/TypeScript-1C1F1C?style=flat-square&logo=typescript&logoColor=7A8F5C&labelColor=1C1F1C"/>
<img src="https://img.shields.io/badge/Vite-1C1F1C?style=flat-square&logo=vite&logoColor=A9856B&labelColor=1C1F1C"/>
<img src="https://img.shields.io/badge/Spring_Boot-1C1F1C?style=flat-square&logo=springboot&logoColor=7A8F5C&labelColor=1C1F1C"/>
<img src="https://img.shields.io/badge/Java-1C1F1C?style=flat-square&logo=openjdk&logoColor=9B4A55&labelColor=1C1F1C"/>


<details>
<summary><b>🏗️ &nbsp;Arquitectura — tres repos, una sola idea</b></summary>

<br/>

```mermaid
flowchart LR
    U["👥 Grupo<br/>disponibilidad + votos"]:::a --> F["🖥️ huecko-frontend<br/>React · TypeScript · Vite"]
    F -- "REST + JWT" --> B["⚙️ huecko-backend<br/>Spring Boot · Java 17"]
    B --> PG[("🐘 PostgreSQL<br/>Flyway")]
    B --> MG[("🍃 MongoDB<br/>eventos")]
    B -- "X-Huecko-Token<br/>si falla, siguen las reglas" --> IA["🤖 huecko-ai-service<br/>FastAPI · Gemini"]
    F -. "modo demo<br/>sin servidor" .-> D["🧪 datos simulados"]
    classDef a fill:#5a2430,color:#f1e6e2,stroke:#9B4A55
    classDef default fill:#1C1F1C,color:#C9C2B0,stroke:#7A8F5C
```

- **La IA no es un punto de falla:** el servicio no guarda datos; si Gemini tarda o se cae, el backend sigue con sus reglas.
- **Persistencia híbrida:** lo relacional en PostgreSQL (con migraciones Flyway), los eventos en MongoDB.
- **Tres formas de arrancar el front:** conectado (proxy de Vite → Spring Boot), `dev:stub` (backend de mentira) y `dev:demo` (sin servidor).
- **El admin observa, no gestiona:** resumen, salud de las bases, fallos y consola en vivo, sin secretos.

</details>

<details>
<summary><b>🗳️ &nbsp;Vida de un plan — del hueco al imprevisto</b></summary>

<br/>

```mermaid
stateDiagram-v2
    direction LR
    state "Disponibilidad" as D
    state "Propuesta" as P
    state "Votación" as V
    state "Confirmado" as C
    state "Imprevisto" as I
    state "Votación exprés" as VE
    [*] --> D: horario manual u OCR
    D --> P: 2–5 ventanas sobre el umbral
    P --> V
    V --> C: gana una ventana
    C --> I: alguien se cae
    I --> VE: con plazo
    VE --> C: MANTENER
    VE --> P: REAGENDAR
    VE --> [*]: CANCELAR
    C --> [*]: el plan pasa ✨
```

La IA lee el motivo de la ausencia, decide si es **crítica** y sugiere `MANTENER`, `REAGENDAR` o `CANCELAR` — con los hechos del aviso, no con los votos.

</details>

<details>
<summary><b>🏷️ &nbsp;Releases</b></summary>

<br/>

| Versión | Qué trajo |
|---|---|
| `v0.5.0` | **IA y despliegue** — servicio de IA con Gemini, front + back + IA publicados |
| `v0.4.0` | **Panel de administración** — resumen, salud, fallos y consola en vivo |

</details>

**Repos:** [`huecko-frontend`](https://github.com/Nakusuo/huecko-frontend) · [`huecko-backend`](https://github.com/Nakusuo/huecko-backend) · [`huecko-ai-service`](https://github.com/Nakusuo/huecko-ai-service)

</details>

<details>
<summary><b>🛡️ &nbsp;SafeZone</b> &nbsp;—&nbsp; plataforma de apoyo a víctimas de violencia</summary>

<br/>

<a href="https://github.com/Nakusuo/SafeZone_Frontend">
  <img src="./assets/safezone.svg" width="100%" alt="SafeZone — botón de pánico con cuenta regresiva"/>
</a>


Cuatro roles, cuatro dashboards: administradora, víctima, psicóloga y defensor
legal. Arquitectura *feature-based* pensada para que cada dominio crezca por
separado.

- **Botón de pánico** flotante con geolocalización GPS, alternativa manual y
  countdown de 10s antes del auto-envío
- **Panel de alertas en tiempo real** para que las profesionales atiendan y
  resuelvan casos
- Gestión de denuncias por tipo de violencia
- Modo mock ↔ backend real conmutable por variable de entorno

<img src="https://img.shields.io/badge/React_18-1C1F1C?style=flat-square&logo=react&logoColor=7A8F5C&labelColor=1C1F1C"/>
<img src="https://img.shields.io/badge/TypeScript-1C1F1C?style=flat-square&logo=typescript&logoColor=7A8F5C&labelColor=1C1F1C"/>
<img src="https://img.shields.io/badge/Tailwind-1C1F1C?style=flat-square&logo=tailwindcss&logoColor=A9856B&labelColor=1C1F1C"/>
<img src="https://img.shields.io/badge/Spring_Boot-1C1F1C?style=flat-square&logo=springboot&logoColor=7A8F5C&labelColor=1C1F1C"/>


<details>
<summary><b>🚨 &nbsp;Así viaja una alerta de pánico</b></summary>

<br/>

```mermaid
sequenceDiagram
    autonumber
    actor V as Víctima
    participant App as SafeZone
    participant API as Spring Boot
    actor P as Profesional
    V->>App: pulsa SOS
    App->>App: GPS (o dirección manual)<br/>countdown 10 s
    App->>API: POST /api/emergency/alerts
    API-->>P: aparece en el panel de alertas
    P->>API: PATCH …/attend
    P->>API: PATCH …/resolve
    API-->>V: caso atendido ✔
```

```text
src/
├── core/       → auth, apiClient, router
├── features/   → admin · auth · victim · psychologist · defender · shared-features
├── shared/     → UI, tipos, utilidades
└── data/       → mockData.json  (VITE_USE_MOCK=true)
```

</details>

**Repo:** [`SafeZone_Frontend`](https://github.com/Nakusuo/SafeZone_Frontend)

</details>

<details>
<summary><b>🩺 &nbsp;Clínica Biométrica</b> &nbsp;—&nbsp; telemedicina con login facial</summary>

<br/>

<a href="https://github.com/Nakusuo/Backend-ClinicaBiometrica">
  <img src="./assets/clinica.svg" width="100%" alt="Clínica Biométrica — login facial"/>
</a>


API de telemedicina: pacientes, doctores, citas y expedientes, con
autenticación JWT y un endpoint de *facial-login*. Documentada en Swagger
desde el primer commit. El frontend va en Angular 16 con videollamadas WebRTC.

<img src="https://img.shields.io/badge/Python-1C1F1C?style=flat-square&logo=python&logoColor=9B4A55&labelColor=1C1F1C"/>
<img src="https://img.shields.io/badge/FastAPI-1C1F1C?style=flat-square&logo=fastapi&logoColor=7A8F5C&labelColor=1C1F1C"/>
<img src="https://img.shields.io/badge/PostgreSQL-1C1F1C?style=flat-square&logo=postgresql&logoColor=C9C2B0&labelColor=1C1F1C"/>
<img src="https://img.shields.io/badge/Angular-1C1F1C?style=flat-square&logo=angular&logoColor=9B4A55&labelColor=1C1F1C"/>


<details>
<summary><b>🧬 &nbsp;Mapa de la API</b></summary>

<br/>

```mermaid
flowchart LR
    A["🅰️ Angular 16<br/>+ WebRTC"] -- "JWT" --> API["⚡ FastAPI<br/>Swagger en /docs"]
    A -- "📷 rostro" --> FL["/auth/facial-login"]
    FL --> API
    API --> R1["pacientes"] & R2["doctores"] & R3["citas"] & R4["expedientes"]
    R1 & R2 & R3 & R4 --> DB[("🐘 PostgreSQL<br/>SQLAlchemy")]
    WH["🔔 webhook /citas"] --> API
    classDef default fill:#1C1F1C,color:#C9C2B0,stroke:#9B4A55
```

</details>

**Repos:** [`Backend-ClinicaBiometrica`](https://github.com/Nakusuo/Backend-ClinicaBiometrica) · [`Frontend-ClinicaBiometrica`](https://github.com/Nakusuo/Frontend-ClinicaBiometrica)

</details>

<details>
<summary><b>📚 &nbsp;Universidad y prácticas</b></summary>

<br/>

Repos de curso donde voy dejando ejercicios y entregas: `ProyectoMesaDePartes`, `CHALK`,
`Lenguajes_Programacion-Frontend`, `semana14-DWI`, `Semana-11-appMovil` y
`Estrucutra-de-datos---Cafeteria`. No son portafolio, son el registro de cómo voy aprendiendo.

</details>

<details>
<summary><b>🌙 &nbsp;Cosas que hice para alguien</b></summary>

<br/>

Páginas pequeñas hechas a mano, sin framework y sin motivo práctico: `4Skate`, `5minutos`, `5555`.
Están ahí por si alguien las encuentra.

</details>

<img src="./assets/divider.svg" width="100%" alt=""/>

## `>` stack

<table>
  <tr>
    <td align="center" width="130"><sub><b>FRONT</b></sub></td>
    <td><img src="https://skillicons.dev/icons?i=ts,react,tailwind,vite,angular,html,css&theme=dark" alt="frontend"/></td>
  </tr>
  <tr>
    <td align="center"><sub><b>BACK</b></sub></td>
    <td><img src="https://skillicons.dev/icons?i=java,spring,py,fastapi,postgres,mongodb&theme=dark" alt="backend"/></td>
  </tr>
  <tr>
    <td align="center"><sub><b>DISEÑO</b></sub></td>
    <td><img src="https://skillicons.dev/icons?i=figma,ps,ai,blender,ae&theme=dark" alt="diseño"/></td>
  </tr>
  <tr>
    <td align="center"><sub><b>HERRAMIENTAS</b></sub></td>
    <td><img src="https://skillicons.dev/icons?i=git,github,githubactions,docker,vscode,idea&theme=dark" alt="herramientas"/></td>
  </tr>
</table>


<details open>
<summary><b>Lo que uso a diario</b></summary>

<br/>

<img src="https://img.shields.io/badge/TypeScript-1C1F1C?style=for-the-badge&logo=typescript&logoColor=7A8F5C&labelColor=1C1F1C"/>
<img src="https://img.shields.io/badge/React-1C1F1C?style=for-the-badge&logo=react&logoColor=7A8F5C&labelColor=1C1F1C"/>
<img src="https://img.shields.io/badge/Tailwind-1C1F1C?style=for-the-badge&logo=tailwindcss&logoColor=A9856B&labelColor=1C1F1C"/>
<img src="https://img.shields.io/badge/Vite-1C1F1C?style=for-the-badge&logo=vite&logoColor=A9856B&labelColor=1C1F1C"/>
<img src="https://img.shields.io/badge/Java-1C1F1C?style=for-the-badge&logo=openjdk&logoColor=9B4A55&labelColor=1C1F1C"/>
<img src="https://img.shields.io/badge/Spring_Boot-1C1F1C?style=for-the-badge&logo=springboot&logoColor=7A8F5C&labelColor=1C1F1C"/>
<img src="https://img.shields.io/badge/Python-1C1F1C?style=for-the-badge&logo=python&logoColor=9B4A55&labelColor=1C1F1C"/>
<img src="https://img.shields.io/badge/FastAPI-1C1F1C?style=for-the-badge&logo=fastapi&logoColor=7A8F5C&labelColor=1C1F1C"/>
<img src="https://img.shields.io/badge/PostgreSQL-1C1F1C?style=for-the-badge&logo=postgresql&logoColor=C9C2B0&labelColor=1C1F1C"/>
<img src="https://img.shields.io/badge/Git-1C1F1C?style=for-the-badge&logo=git&logoColor=9B4A55&labelColor=1C1F1C"/>

</details>

<details>
<summary><b>Diseño y visuales</b></summary>

<br/>

<img src="https://img.shields.io/badge/Figma-1C1F1C?style=for-the-badge&logo=figma&logoColor=A9856B&labelColor=1C1F1C"/>
<img src="https://img.shields.io/badge/Photoshop-1C1F1C?style=for-the-badge&logo=adobephotoshop&logoColor=C9C2B0&labelColor=1C1F1C"/>
<img src="https://img.shields.io/badge/Illustrator-1C1F1C?style=for-the-badge&logo=adobeillustrator&logoColor=A9856B&labelColor=1C1F1C"/>
<img src="https://img.shields.io/badge/Krita-1C1F1C?style=for-the-badge&logo=krita&logoColor=7A8F5C&labelColor=1C1F1C"/>
<img src="https://img.shields.io/badge/Blender-1C1F1C?style=for-the-badge&logo=blender&logoColor=A9856B&labelColor=1C1F1C"/>
<img src="https://img.shields.io/badge/After_Effects-1C1F1C?style=for-the-badge&logo=adobeaftereffects&logoColor=9B4A55&labelColor=1C1F1C"/>

</details>

<details>
<summary><b>En la lista de aprender</b></summary>

<br/>

<img src="https://img.shields.io/badge/Docker-1C1F1C?style=for-the-badge&logo=docker&logoColor=C9C2B0&labelColor=1C1F1C"/>
<img src="https://img.shields.io/badge/Next.js-1C1F1C?style=for-the-badge&logo=nextdotjs&logoColor=C9C2B0&labelColor=1C1F1C"/>
<img src="https://img.shields.io/badge/Testing-1C1F1C?style=for-the-badge&logo=vitest&logoColor=7A8F5C&labelColor=1C1F1C"/>
<img src="https://img.shields.io/badge/Three.js-1C1F1C?style=for-the-badge&logo=threedotjs&logoColor=A9856B&labelColor=1C1F1C"/>

</details>

<img src="./assets/divider.svg" width="100%" alt=""/>

## `>` métricas

<div align="center">

<img width="98%" src="./profile-summary-card-output/kacho_ga/0-profile-details.svg" alt="resumen"/>

<img height="190" src="./profile-summary-card-output/kacho_ga/3-stats.svg" alt="stats"/>
<img height="190" src="./profile-summary-card-output/kacho_ga/2-most-commit-language.svg" alt="lenguajes por commits"/>

<img height="190" src="./profile-summary-card-output/kacho_ga/1-repos-per-language.svg" alt="repos por lenguaje"/>
<img height="190" src="./profile-summary-card-output/kacho_ga/4-productive-time.svg" alt="horas productivas"/>


<img height="190" src="https://streak-stats.demolab.com/?user=Nakusuo&hide_border=true&background=15171A&stroke=2C322C&ring=7A8F5C&fire=9B4A55&currStreakNum=C9C2B0&sideNums=C9C2B0&currStreakLabel=8FA36B&sideLabels=A9856B&dates=6F776A&locale=es" alt="racha de commits"/>

</div>

<img src="./assets/divider.svg" width="100%" alt=""/>

## `>` mis commits, pero como videojuego

<div align="center">
  <img src="https://raw.githubusercontent.com/Nakusuo/Nakusuo/output/github-snake-dark.svg" alt="snake" width="100%"/>
</div>

<div align="center">
  <img src="./profile-3d-contrib/profile-night-green.svg" alt="grafo 3D de contribuciones" width="100%"/>
</div>

<img src="./assets/divider.svg" width="100%" alt=""/>

## `>` últimos movimientos

<!--START_SECTION:activity-->
1. 🎉 Merged PR [#2](https://github.com/Nakusuo/dotfiles/pull/2) in [Nakusuo/dotfiles](https://github.com/Nakusuo/dotfiles)
2. 💪 Opened PR [#2](https://github.com/Nakusuo/dotfiles/pull/2) in [Nakusuo/dotfiles](https://github.com/Nakusuo/dotfiles)
3. 🎉 Merged PR [#1](https://github.com/Nakusuo/dotfiles/pull/1) in [Nakusuo/dotfiles](https://github.com/Nakusuo/dotfiles)
4. 💪 Opened PR [#1](https://github.com/Nakusuo/dotfiles/pull/1) in [Nakusuo/dotfiles](https://github.com/Nakusuo/dotfiles)
5. 🚀 Published release [v0.5.0 · IA y despliegue](https://github.com/Nakusuo/huecko-ai-service/releases/tag/v0.5.0) in [Nakusuo/huecko-ai-service](https://github.com/Nakusuo/huecko-ai-service)
<!--END_SECTION:activity-->

<img src="./assets/divider.svg" width="100%" alt=""/>

<a name="side-b"></a>

<details>
<summary><sub><code>▸ side B</code></sub></summary>

<br/>

<img src="./assets/side-b.svg" width="100%" alt="side B — pistas ocultas"/>

```text
 ┌──────────────────────────────────────────────┐
 │  cinta encontrada en una carpeta sin nombre  │
 │                                              │
 │  05  commits a las 2am                       │
 │  06  "arreglo esto mañana" (no lo arregló)   │
 │  07  el CSS que sí funcionó a la primera     │
 │  08  ruido blanco                            │
 └──────────────────────────────────────────────┘
```

Si estás leyendo esto es porque abriste el desplegable. Bien hecho. `|-/`

</details>

<img src="./assets/footer.svg" width="100%" alt="Fin de la cara A — dale la vuelta a la cinta"/>

<div align="center">
  <sub><code>~/Nakusuo</code> &nbsp;·&nbsp; construido con demasiado café y atajos de teclado ☕</sub>
</div>
