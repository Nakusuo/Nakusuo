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

<br/>

<img src="https://readme-typing-svg.demolab.com?font=VT323&size=30&pause=1400&color=8FA36B&center=true&vCenter=true&width=560&lines=Estudiante+de+Ingenier%C3%ADa+de+Software;Frontend+en+React+%2B+TypeScript;Backend+en+Spring+Boot+y+FastAPI;Dise%C3%B1o%2C+arte+y+c%C3%B3digo+creativo" alt="typing"/>

</div>

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

<img src="./assets/divider.svg" width="100%" alt=""/>

## `>` en qué ando

<details open>
<summary><b>🗓️ &nbsp;Huecko</b> &nbsp;—&nbsp; coordinar planes entre amigos sin 40 mensajes de WhatsApp</summary>

<br/>

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

**Repos:** [`huecko-frontend`](https://github.com/Nakusuo/huecko-frontend) · [`huecko-backend`](https://github.com/Nakusuo/huecko-backend) · [`huecko-ai-service`](https://github.com/Nakusuo/huecko-ai-service)

</details>

<details>
<summary><b>🛡️ &nbsp;SafeZone</b> &nbsp;—&nbsp; plataforma de apoyo a víctimas de violencia</summary>

<br/>

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

**Repo:** [`SafeZone_Frontend`](https://github.com/Nakusuo/SafeZone_Frontend)

</details>

<details>
<summary><b>🩺 &nbsp;Clínica Biométrica</b> &nbsp;—&nbsp; telemedicina con login facial</summary>

<br/>

API de telemedicina: pacientes, doctores, citas y expedientes, con
autenticación JWT y un endpoint de *facial-login*. Documentada en Swagger
desde el primer commit. El frontend va en Angular 16 con videollamadas WebRTC.

<img src="https://img.shields.io/badge/Python-1C1F1C?style=flat-square&logo=python&logoColor=9B4A55&labelColor=1C1F1C"/>
<img src="https://img.shields.io/badge/FastAPI-1C1F1C?style=flat-square&logo=fastapi&logoColor=7A8F5C&labelColor=1C1F1C"/>
<img src="https://img.shields.io/badge/PostgreSQL-1C1F1C?style=flat-square&logo=postgresql&logoColor=C9C2B0&labelColor=1C1F1C"/>
<img src="https://img.shields.io/badge/Angular-1C1F1C?style=flat-square&logo=angular&logoColor=9B4A55&labelColor=1C1F1C"/>

**Repos:** [`Backend-ClinicaBiometrica`](https://github.com/Nakusuo/Backend-ClinicaBiometrica) · [`Frontend-ClinicaBiometrica`](https://github.com/Nakusuo/Frontend-ClinicaBiometrica)

</details>

<details>
<summary><b>📚 &nbsp;Universidad y prácticas</b></summary>

<br/>

Repos de curso donde voy dejando ejercicios y entregas: `Lenguajes_Programacion-Frontend`,
`semana14-DWI`, `5minutos`, `Estrucutra-de-datos---Cafeteria`. No son portafolio,
son el registro de cómo voy aprendiendo.

</details>

<img src="./assets/divider.svg" width="100%" alt=""/>

## `>` stack

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
1. 🎉 Merged PR [#12](https://github.com/Nakusuo/huecko-backend/pull/12) in [Nakusuo/huecko-backend](https://github.com/Nakusuo/huecko-backend)
2. 💪 Opened PR [#12](https://github.com/Nakusuo/huecko-backend/pull/12) in [Nakusuo/huecko-backend](https://github.com/Nakusuo/huecko-backend)
3. 🎉 Merged PR [#23](https://github.com/Nakusuo/huecko-frontend/pull/23) in [Nakusuo/huecko-frontend](https://github.com/Nakusuo/huecko-frontend)
4. 💪 Opened PR [#23](https://github.com/Nakusuo/huecko-frontend/pull/23) in [Nakusuo/huecko-frontend](https://github.com/Nakusuo/huecko-frontend)
5. 🎉 Merged PR [#11](https://github.com/Nakusuo/huecko-backend/pull/11) in [Nakusuo/huecko-backend](https://github.com/Nakusuo/huecko-backend)
<!--END_SECTION:activity-->

<img src="./assets/divider.svg" width="100%" alt=""/>

<details>
<summary><sub><code>▸ side B</code></sub></summary>

<br/>

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

<div align="center">
  <sub><code>~/Nakusuo</code> &nbsp;·&nbsp; construido con demasiado café y atajos de teclado ☕</sub>
</div>
