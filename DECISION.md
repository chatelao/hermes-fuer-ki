# DECISION Log

## 2025-05-15 14:30 - Specification Conversion Strategy
- **Problem**: Convert downloaded specifications (HTML and PDF) to Markdown for readability and AI consumption, as required by GEMINI.md.
- **Solution 1**: Use `lynx -dump` for HTML and `strings` for PDF.
  - Reasoning: Uses pre-installed tools but results in poor formatting and potential data loss for PDFs.
- **Solution 2 (Chosen)**: Use `html2text` for HTML and `pdfminer.six` (`pdf2txt.py`) for PDF.
  - Reasoning: These specialized libraries provide much better Markdown/text conversion quality, preserving structure and links better than generic tools.
- **Solution 3**: Manual conversion/transcription.
  - Reasoning: Extremely time-consuming and prone to human error, although high quality.

## 2024-03-14 10:45 - Fifth Framework Choice
- **Problem**: GEMINI.md requires adding one more framework of choice to the fusion list.
- **Solution 1 (Chosen)**: PRINCE2. It is a widely recognized, process-based method for effective project management that complements the existing list well, especially Hermes and RUP.
- **Solution 2**: Kanban. While useful, it is often seen as a subset or complement to Scrum rather than a full process framework like the others.
- **Solution 3**: Extreme Programming (XP). Strong on technical practices, but Scrum already covers much of the agile perspective needed.
- **Reasoning**: PRINCE2 provides a strong governance and process-oriented structure that fits well with the project's goal of creating a comprehensive RACI and skill framework.

## 2024-03-14 10:45 - Project Bootstrapping
- **Problem**: Initialize the project according to GEMINI.md.
- **Solution 1 (Chosen)**: Manual creation of the directory structure and initial markdown files based on the project structure section in GEMINI.md.
- **Reasoning**: This ensures full compliance with the specified layout from the start.

## 2024-03-14 12:25 - Framework Specification Acquisition
- **Problem**: Obtain authentic specifications for RUP, V-Modell-XT, Hermes, SCRUM, and PRINCE2.
- **Solution 1**: Direct download from official websites.
- **Solution 2**: Retrieval from the Internet Archive (Wayback Machine).
- **Solution 3 (Chosen)**: Use a hybrid approach of official downloads and comprehensive educational/reference summaries (e.g., Wikipedia) when direct official PDFs are unavailable or restricted by access controls.
- **Reasoning**: While official PDFs are preferred, many are behind paywalls or restricted by automated access controls. High-quality summaries ensure the project has the necessary conceptual information to build the fusion framework.
