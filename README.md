# LangChainJ

**개발기간**: 2024-05-19 ~ 2024-06-05

LangChainJ는 LangChain의 핵심 기능을 Python으로 직접 구현한 프로젝트로, 문서 기반 질의응답 시스템(RAG: Retrieval-Augmented Generation)의 핵심 구성 요소를 단계적으로 설계하고 학습하는 데 목적이 있습니다.

## 🧠 핵심 구성

이 프로젝트는 LangChain에서 사용하는 주요 모듈들을 분리하여 자체적으로 구현하였습니다:

- **Document Loader**: PDF, 텍스트 파일 등을 불러오는 기능
- **Text Splitter**: 긴 문서를 처리하기 위한 청크 분할
- **Embedding Generator**: 임베딩 API를 활용한 텍스트 벡터화
- **Vector Store**: FAISS를 이용한 벡터 저장 및 검색
- **LLM Wrapper**: OpenAI API 기반 LLM 호출

## 🗂️ 디렉토리 구조

```
LangChainJ/
│
├── document_loaders/      # 파일 로더 (PDF 등)
├── embeddings/            # 임베딩 생성 모듈
├── text_splitters/        # 텍스트 분할기
├── vectorstores/          # 벡터 DB 래퍼
├── openai/                # OpenAI API 래퍼
├── rag.py                 # 전체 RAG 파이프라인 실행 예시
├── requirements.txt
└── README.md
```

> **주의**: `.env` 또는 환경변수를 통해 OpenAI API Key가 필요합니다.
```bash
export OPENAI_API_KEY=your_openai_key
```

해당 스크립트는 다음 단계를 순차적으로 수행합니다:
1. 문서 로딩
2. 텍스트 분할
3. 임베딩 생성
4. 벡터 저장소 구축
5. 사용자 쿼리에 대해 관련 문서를 검색 후 LLM으로 답변 생성

## 📌 사용 기술

- Python 3.10+
- OpneAI
- OpenAI Embeddings
- PyPDF2
- ...

## 🤝 프로젝트 목적

이 프로젝트는 제가 LangChain의 구조를 직접 구현하며 **RAG 시스템의 핵심 원리를 깊이 있게 이해하고**, 프레임워크를 분석 및 구현하여 오픈 소스를 분석하는 능력을 기르고, 상용 프레임워크 없이도 이러한 구조를 어떻게 구성할 수 있는지 학습하는 데 중점을 두고 있습니다.

### 구현한 주요 내용

- 각 구성 요소를 모듈 단위로 분리하여 재사용성과 확장성을 높임
- 외부 라이브러리에 의존하지 않고 PDF 로딩부터 벡터 저장소 검색까지 전체 파이프라인 직접 구성
- LangChain의 아키텍처를 참고하되, 내부 로직을 파악하며 유사하게 재구성함으로써 개념적 이해 강화
- LangChain 의 문자열 회귀 문자 분리 로직을 학습하여 스스로의 이해 바탕으로 텍스트 분리 모듈 구현

이 프로젝트는 저의 RAG 시스템 구조 설계 및 실습 기반 학습 기록이자, 향후 개인화된 지식 질의응답 시스템 개발을 위한 기초 플랫폼입니다.

