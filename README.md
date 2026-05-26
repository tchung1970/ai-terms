# AI 용어집

AI 시대를 살아남기 위한 단어들의 안내서.

🌐 **Live:** https://ai.tchung.org/ai-terms/

**원문** [A survival guide to the words behind the AI boom](https://www.businessinsider.com/ai-terms-definitions-glossary) · **출처** Business Insider · **번역** 2026.05.26

---

## 무엇인가요

AI 시대를 이해하기 위한 핵심 용어와 인물 53개를 한국어로 정리했습니다.

- **38개 용어** — Agentic AI, AGI, Alignment … World Models
- **15명의 인물** — Sam Altman, Dario Amodei … Mark Zuckerberg
- 카테고리 태그(개념 · 기술 · 모델 · 리스크 · 정책 · 문화)로 분류
- 한국어 · 영문 · 설명 전체를 가로지르는 즉시 검색

## 특징

- 순수 정적 사이트 — 단일 HTML 파일, 빌드 도구 없음
- 모바일 우선 반응형 디자인
- Pretendard 본문, Gowun Batang 데코
- 1200×630 OG 이미지 (`og.png`) 자동 포함 — Threads/Twitter 미리보기 대응

## 구조

```
ai-terms/
├── index.html    # 사이트 전체 (HTML · CSS · 데이터 · 로직)
├── og.png        # 소셜 미리보기 이미지 (1200×630)
├── make_og.py    # og.png 생성 스크립트 (PIL)
└── README.md
```

데이터(용어·인물)는 `index.html` 내 `TERMS`, `PEOPLE` 배열에 있습니다.

## 로컬 미리보기

```bash
python3 -m http.server 8000
# → http://localhost:8000
```

---

<sub>Claude Opus 4.7 · [GitHub](https://github.com/tchung1970/ai-terms)</sub>
