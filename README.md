# 🚀 FinTech AI for Financial Inclusion: "Financial Identity for Everyone"

> **AI Build-a-thon 2025 - FinTech Track**
> *Building a transparent, bias-aware, and inclusive financial ecosystem for the 100M+ unbanked.*

![Project Banner](https://img.shields.io/badge/Status-Prototype_Ready-success) ![License](https://img.shields.io/badge/License-MIT-blue) ![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Next.js](https://img.shields.io/badge/Next.js-14-black)

## 📋 Table of Contents
- [Vision](#-vision)
- [Key Innovation: TrustGraph AI](#-key-innovation-trustgraph-ai)
- [System Architecture](#-system-architecture)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation & Setup](#-installation--setup)
- [API Documentation](#-api-documentation)
- [Roadmap](#-roadmap)

---

## 👁️ Vision
Our mission is to democratize access to credit for unbanked individuals in Bangladesh. Traditional banking relies on collateral and credit history—things the poor don't have. Our solution leverages **Alternative Data** (mobile usage, transactions) and **Social Trust** to build a digital financial identity.

**Core Philosophy:**
1.  **Inclusion**: No digital footprint? No problem.
2.  **Transparency**: Explaining *why* a loan is approved or denied.
3.  **Community**: Leveraging social capital as collateral.

---

## 🦄 Key Innovation: "TrustGraph AI"
We introduce a **10x Feature** called **TrustGraph™**.
In rural economies, "Trust" is currency. We digitized this by analyzing social connections.
- **How it works**: If a user is vouched for by community leaders or responsible borrowers, their credit score receives a **"Social Trust Boost"**.
- **Impact**: Solves the "Cold Start" problem for first-time borrowers with zero transaction history.

---

## 🏗 System Architecture
The solution is built as a modular Monorepo:

### 1. Data Layer
- **Usage Data**: Mobile top-ups, transaction frequency, wallet balance.
- **Social Data**: Community referrals and group savings behavior.

### 2. Intelligence Core (Python/FastAPI)
- **Model**: Random Forest Regressor trained on synthetic financial inclusions data.
- **Explainability**: SHAP (Shapley Additive Explanations) to provide individual feature contribution scores.

### 3. Application Layer (Next.js)
- **MFI Dashboard**: For loan officers to assess risk and view AI explanations.
- **Voice Companion**: An embedded assistant for borrowers (simulated) to increase accessibility for the illiterate.

---

## ✨ Features

### 🏦 For MFI Officers (Dashboard)
- **Dynamic Credit Score**: Scored from **300 to 900**.
- **Risk Classification**: Low (Green), Medium (Yellow), High (Red).
- **Explainable AI Integration**:
  - *"Why is this score low?"* -> "Low average monthly top-up (-50 pts)."
  - *"Why is this score high?"* -> "Strong community backing (+100 pts)."

### 🗣️ For Borrowers (App/IVR)
- **Voice Finance Companion**: A Bangla-speaking assistant helping users understand their credit health.
- **TrustGraph Verification**: Visual badge showing community trust level.

---

## 🛠 Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Backend** | **FastAPI** | High-performance Python API framework. |
| **ML Engine** | **Scikit-Learn** | Random Forest implementation. |
| **XAI** | **SHAP** | Explainable AI library. |
| **Frontend** | **Next.js 14** | React Framework with App Router. |
| **Styling** | **Tailwind CSS** | Utility-first CSS framework. |
| **Icons** | **Lucide React** | Beautiful & consistent icons. |

---

## ⚡ Installation & Setup

### Prerequisites
- Node.js (v18+)
- Python (v3.9+)
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/XidanAbds29/Ai-buidathon.git
cd Ai-buidathon
```

### 2. Backend Setup
The backend serves the AI models and API.

```bash
cd backend
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate
# Activate (Mac/Linux)
# source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Train the AI Model (Required for first run)
python train_model.py

# Run the Server
python -m uvicorn main:app --reload
```
*Backend runs at `http://localhost:8000`*

### 3. Frontend Setup
The frontend is the MFI Dashboard.

```bash
cd frontend
# Install dependencies
npm install

# Run Development Server
npm run dev
```
*Frontend runs at `http://localhost:3000`*

---

## 📡 API Documentation

### `POST /score`
Calculate credit score based on user data.
**Body:**
```json
{
  "user_id": "string",
  "wallet_balance": 5000,
  "avg_monthly_topup": 200,
  "transaction_count_last_90_days": 45,
  "community_trust_referrals": 2,
  "has_smart_phone": true,
  "age": 30
}
```

### `POST /explain`
Get textual explanation for the score.
**Body:** Same as `/score`.
**Response:**
```json
{
  "narrative_explanation": "Score impacted positively by...",
  "top_positive_factors": ["High Trust..."],
  "top_negative_factors": ["Low Balance..."]
}
```

---

## 🗺️ Roadmap
- [x] **Phase 1**: Prototype (Current) - Basic scoring and dashboard.
- [ ] **Phase 2**: Pilot - Integration with real SMS/Telco APIs.
- [ ] **Phase 3**: Scale - National rollout with 100k+ users.

---

## 🤝 Contribution
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

© 2025 AI Build-a-thon Team.
