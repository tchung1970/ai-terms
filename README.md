# AI 용어집 · AI Terms in Korean

AI 시대를 살아남기 위한 단어들의 안내서.
Business Insider의 AI 용어 사전을 한국어로 옮긴 정적 사이트입니다.

🌐 **Live:** https://ai.tchung.org/ai-terms/

📰 **원문:** [A survival guide to the words behind the AI boom](https://www.businessinsider.com/ai-terms-definitions-glossary) — Business Insider · Brent D. Griffiths, Aaron Mok, Jyoti Mann, Grace Eliza Goodwin

---

## 📖 무엇인가요

AI의 부상은 기술 자체만큼이나 빠르게 변하는 새로운 어휘를 만들어냈습니다.
이 사이트는 동료들과의 대화에서, 뉴스 기사 앞에서, 회의에서 AI를 이야기하기 위해
알아두면 좋은 핵심 용어와 인물 53개를 한국어로 정리합니다.

- **38개 용어** — Agentic AI, AGI, Alignment, … World Models
- **15명의 인물** — Sam Altman, Dario Amodei, … Mark Zuckerberg
- 카테고리 태그(개념 · 기술 · 모델 · 리스크 · 정책 · 문화)로 한눈에 분류
- 한국어 · 영문 · 설명 전체를 가로지르는 즉시 검색

## ✨ 특징

- **순수 정적 사이트** — 단일 HTML 파일, 빌드 도구 없음
- **모바일 우선 반응형** 디자인
- **Pretendard** 한글 본문 폰트 + **Gowun Batang** 데코 세리프
- 부드러운 오프화이트 배경 + 5색 카테고리 팔레트 (자두 · 장미 · 잎 · 바다 · 호박)
- 클라이언트 사이드 검색 / 필터 / 하이라이트 — 자바스크립트 한 파일에 모든 데이터 포함

## 🚀 사용법

별도의 빌드가 필요 없습니다. `index.html`을 브라우저에서 열거나, 정적 호스팅에 올리면 됩니다.

```bash
# 로컬에서 미리보기
python3 -m http.server 8000
# → http://localhost:8000
```

## 📁 구조

```
ai-terms/
├── index.html   # 사이트 전체 (HTML · CSS · 데이터 · 로직)
└── README.md
```

데이터(용어·인물)는 `index.html` 내 `TERMS`, `PEOPLE` 배열에 있습니다.
새 용어를 추가하거나 번역을 수정하려면 해당 배열을 편집하면 됩니다.

## 📝 라이선스 및 출처

- 원문 텍스트와 정의의 저작권은 **Business Insider** 및 원저자에게 있습니다.
- 본 저장소는 학습·교육 목적의 **한국어 번역**이며, 상업적 이용을 의도하지 않습니다.
- 코드(HTML·CSS·JS)는 자유롭게 참고하셔도 됩니다.

---

*Translated and built with [Claude](https://claude.com/claude-code) · 2026.05*
