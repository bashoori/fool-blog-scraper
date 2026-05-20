# Motley Fool Blog Scraper & Analyzer

Financial news aggregation and sentiment analysis platform: scrape investment blogs, extract investment theses, track sentiment trends, and identify emerging investment themes.

## Overview

Financial blogs like Motley Fool publish investment ideas daily, but aggregating and analyzing this content manually is time-consuming. This project automatically scrapes articles, extracts investment theses, performs sentiment analysis, and identifies emerging themes.

**Key Topics**
- Web scraping (blog content extraction)
- NLP and sentiment analysis
- Investment theme extraction
- Trend detection in financial writing
- Time-series sentiment tracking

## Problem It Solves

Investors want to:
- Stay informed about investment ideas
- Understand the investment thesis for hot stocks
- Track sentiment trends (bullish vs. bearish market)
- Identify emerging investment themes early
- Aggregate multiple blog sources

**Manual approach:** Read multiple blogs daily, track sentiment manually.  
**Automated approach:** Scraper aggregates content, NLP extracts themes, trends are automatically detected.

## Architecture

### Scraping
- Fetch latest blog articles
- Extract: title, author, publish date, content, ticker mentions
- Parse HTML to clean content (remove navigation, ads, etc.)
- Store raw articles for analysis

### Processing
- Tokenize and normalize text
- Extract stock ticker mentions (AAPL, TSLA, etc.)
- Identify investment themes (growth, value, dividend, tech, etc.)
- Extract key statistics and quotes

### Analysis
- Sentiment scoring (bullish, neutral, bearish)
- Theme frequency (which themes are hot?)
- Stock sentiment aggregation (how much coverage, overall tone?)
- Trend detection (sentiment shifting?)

### Output
- **Sentiment report** — overall market sentiment by theme
- **Stock alerts** — high-conviction ideas with consistent coverage
- **Theme trends** — which investment ideas are emerging
- **Author tracking** — which writers are most accurate
- **CSV export** — all articles with metadata and sentiment

## Key Features (Enhanced)

### 1. Article Extraction
- Parse blog posts and extract:
  - Title, author, date
  - Main investment thesis
  - Stock tickers mentioned
  - Risk/reward assessment
  - Target price (if mentioned)

### 2. Sentiment Analysis
- Bullish vs. bearish language
- Confidence level (strong conviction vs. uncertain)
- Risk assessment (downside risk highlighted?)
- Compare sentiment over time (tracking changes)

### 3. Stock-Level Aggregation
- Combine all mentions of a stock
- Calculate net sentiment (bullish articles - bearish articles)
- Track coverage frequency (hot stocks get more mentions)
- Identify consensus views

### 4. Theme Extraction
Investment themes:
- **Growth stocks** — high growth, high P/E
- **Value stocks** — low P/E, stable dividends
- **Dividend plays** — income-focused
- **Tech trends** — AI, cloud, semiconductors, etc.
- **Sector trends** — healthcare, energy, finance, etc.

### 5. Contrarian Signals
- Identify consensus vs. outlier views
- Track when opinions shift dramatically
- Flag controversial ideas (strong disagreement)
- Measure conviction (how often is the idea repeated?)

### 6. Time-Series Tracking
- Sentiment trends over months
- Theme popularity over time
- Coverage frequency by stock
- Emerging consensus formation

## Project Structure

```
fool-blog-scraper/
├── scrapers/
│   ├── fool_scraper.py
│   └── content_parser.py
├── nlp/
│   ├── sentiment_analyzer.py
│   ├── theme_extractor.py
│   └── ticker_recognizer.py
├── analysis/
│   ├── stock_sentiment.py
│   ├── theme_trends.py
│   └── consensus_builder.py
├── output/
│   ├── sentiment_report.csv
│   ├── theme_trends.json
│   └── stock_alerts.html
├── data/
│   └── fool_blog_posts.csv
└── README.md
```

## Running It

### Local
```bash
pip install -r requirements.txt

# Scrape latest articles
python scrapers/fool_scraper.py --days 30

# Analyze sentiment
python nlp/sentiment_analyzer.py
python nlp/theme_extractor.py

# Generate reports
python analysis/stock_sentiment.py
python analysis/theme_trends.py

# Output results
python output/generate_reports.py
```

## Sample Outputs

### Sentiment Report
| Stock | Bullish | Neutral | Bearish | Net | Avg Sentiment |
|---|---|---|---|---|---|
| TSLA | 8 | 2 | 3 | +5 | 0.62 (Moderate Bullish) |
| AAPL | 12 | 4 | 2 | +10 | 0.75 (Strong Bullish) |
| META | 3 | 2 | 7 | -4 | -0.40 (Bearish) |

### Theme Trends
```
AI/ML Transformation: ↑↑↑ (30% month growth)
  Mentioned in: AAPL, NVDA, MSFT, GOOGL
  Sentiment: 0.68 (Bullish)
  Emerging: True (gaining traction)

Dividend Stocks: → (stable, high coverage)
  Mentioned in: JNJ, PG, VZ
  Sentiment: 0.45 (Slightly bullish)
  Momentum: Declining (less enthusiasm)
```

### Stock Alert Example
```
🚨 AAPL - Strong Bullish Consensus
Articles: 12 (past 30 days)
Sentiment: 0.75 (Strong Bullish)
Themes: AI, Services Growth, Valuation
Average Target: $195 (vs. current $170)
Conviction: High (consistent across writers)
Latest Take: "Apple's AI strategy positions it for 5-year growth"
```

## What This Demonstrates

**Web Scraping**
- Parsing blog content
- Handling variable HTML structures
- Extraction of structured data from unstructured content

**Natural Language Processing**
- Sentiment analysis (not just positive/negative, but conviction)
- Theme extraction (identifying investment concepts)
- Ticker recognition (finding stock symbols in text)

**Financial Analysis**
- Understanding investment theses
- Aggregating diverse opinions
- Identifying market consensus and outliers

**Time-Series Analysis**
- Tracking sentiment trends
- Identifying shifts in market narrative
- Consensus formation over time

## Enhanced Features Added

✓ **Article extraction** — title, thesis, tickers, sentiment  
✓ **Sentiment analysis** — bullish/bearish/neutral with confidence  
✓ **Stock aggregation** — net sentiment per stock  
✓ **Theme extraction** — identify investment concepts  
✓ **Contrarian signals** — spot outlier opinions  
✓ **Time-series tracking** — sentiment and theme trends  

## Limitations & Considerations

- **Not investment advice** — for research/analysis only
- **Author quality varies** — some writers are more accurate
- **Sentiment analysis imperfect** — NLP isn't perfect
- **Past performance doesn't predict future** — use with caution
- **Bias in blogs** — blogs have inherent biases

## What I'd Do Differently

1. **Multi-source aggregation** — include other financial blogs
2. **Author tracking** — score accuracy of predictions
3. **Consensus backtesting** — did consensus opinions work?
4. **Integration with prices** — correlate sentiment with returns
5. **ML prediction** — predict stock price from sentiment

## Next Steps

- Add author accuracy tracking (who predicts best?)
- Backtest sentiment signals (did bullish articles outperform?)
- Integrate stock price data (compare sentiment vs. performance)
- Multi-source aggregation (Seeking Alpha, TradingView, etc.)
- Real-time alerts (notify of major sentiment shifts)

---

**The point:** Financial data is valuable for investors. This project shows how to aggregate, analyze, and extract actionable intelligence from unstructured financial writing. That's data-driven investing.
