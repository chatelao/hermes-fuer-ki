# DECISION Log

## 2026-03-19 10:00 - Deliverable Template Architecture
- **Problem**: Define the architecture and location for deliverable templates to support the roadmap.
- **Solution 1 (Chosen): Modular YAML Templates in `src/data/templates/`**
  - Reasoning: Providing individual YAML templates for each deliverable, alongside a `project_manifest.yaml` template, allows users to easily bootstrap new projects. Storing them in `src/data/templates/` keeps them organized and separate from active project data while remaining under the `/src/data` umbrella as instances of the schema.
- **Solution 2: Monolithic Template File**
  - Reasoning: Simpler to copy a single file, but inconsistent with the chosen modular project architecture and harder to validate granularly.
- **Solution 3: Embedded Templates in Documentation**
  - Reasoning: Good for quick reference but requires manual copy-pasting and extra steps for users to create valid YAML files.

## 2026-03-18 09:00 - Sample Project Instance Architecture
- **Problem**: Define the architecture for executing a sample project instance as per the roadmap.
- **Solution 1: Monolithic Project YAML**
  - Reasoning: Simple to manage as a single file, but becomes unwieldy as project complexity and deliverable detail grow.
- **Solution 2 (Chosen): Directory-based Modular YAMLs**
  - Reasoning: A `project_manifest.yaml` links to individual deliverable YAML files in a dedicated project directory. This mirrors the framework's modular design, improves human readability/editability of specific documents, and allows for granular schema validation.
- **Solution 3: Interactive State-only JSON**
  - Reasoning: Optimized for tool consumption, but fails the "human ease of interaction" requirement for reviewing and editing deliverables.

## 2026-03-17 10:00 - Detailed Role Descriptions & Interaction Guides Strategy
- **Problem**: Expand the framework to provide detailed role descriptions and interaction guides as per the roadmap.
- **Solution 1 (Chosen): Structured YAML Data with Individual Documentation Pages**
  - Reasoning: By expanding the JSON schema and YAML data, we maintain a machine-readable source of truth while enabling the automated generation of detailed, human-friendly role pages. This approach ensures consistency between the data model and documentation.
- **Solution 2: Monolithic Documentation File**
  - Reasoning: Easier to generate and read in one go, but less scalable as roles become more complex and harder to link to specifically from other parts of the framework.
- **Solution 3: Interactive CLI-only Documentation**
  - Reasoning: Innovative, but fails to provide the persistent, searchable Markdown documentation required for broad accessibility and integration with standard tools.

## 2026-03-16 15:00 - Mermaid Image Generation Strategy
- **Problem**: Implement automated generation of Mermaid diagrams to PNG/SVG in CI/CD.
- **Solution 1 (Chosen): Integrated Python Scripting with Mermaid CLI**
  - Reasoning: Leverages the existing Python-based generation pipeline. Using `mmdc` (Mermaid CLI) directly from the script ensures that documentation and images are always generated from the same source of truth and allows for easy local reproduction of the build process.
- **Solution 2: Dedicated GitHub Action for Mermaid**
  - Reasoning: Simplifies the CI/CD configuration by using a pre-built action, but creates a dependency on a third-party action and makes local image generation more difficult to maintain consistently with the CI environment.
- **Solution 3: Client-side Rendering only**
  - Reasoning: Minimal effort as it relies on Markdown viewers to render diagrams, but fails the requirement to provide static PNG/SVG artifacts for portability and offline use.

## 2026-03-16 14:00 - Framework Verification & Testing Strategy
- **Problem**: Implement comprehensive test cases to verify all framework tasks as specified in the roadmap.
- **Solution 1 (Chosen): Modular Pytest Suite**
  - Reasoning: Implementing separate test files for data integrity, referential integrity, design alignment, and script execution provides a modular and maintainable verification system that clearly identifies failure points.
- **Solution 2: Monolithic Verification Script**
  - Reasoning: Easier to run as a single command, but lacks the granularity and reporting benefits of a standard testing framework like pytest.
- **Solution 3: Validation-Script Centric Testing**
  - Reasoning: Consolidates logic but mixes validation with testing concerns, making it harder to verify the behavior of generation scripts themselves.

## 2026-03-16 13:00 - Documentation & Deliverable Generation Strategy
- **Problem**: Select an approach for generating documentation, RACI matrices, and process diagrams from the YAML source data.
- **Solution 1 (Chosen): Direct Python Scripting (String Interpolation)**
  - Reasoning: Simple, lightweight, and requires no additional dependencies beyond what is already used for validation. It provides sufficient flexibility for generating Markdown and Mermaid files.
- **Solution 2: Template-based Generation (Jinja2)**
  - Reasoning: More robust for complex documentation layouts and separates logic from presentation, but introduces an external dependency.
- **Solution 3: Specialized Documentation Framework (MkDocs/Sphinx)**
  - Reasoning: Provides a professional-grade documentation site, but is likely overkill for the current project scope and adds significant complexity to the build process.

## 2026-03-16 12:00 - Project Data Organization & Schema Validation
- **Problem**: Define the optimal location for the primary framework data and test instances to ensure compliance with `GEMINI.md` and support AI observability.
- **Solution 1: Framework definition in `/src/schema`**
  - Reasoning: Keeps the schema and its primary instance together, but violates the directory purpose defined in `GEMINI.md`.
- **Solution 2: Hierarchical hybrid structure**
  - Reasoning: Organizes data into subdirectories by framework or version. While scalable for very large projects, it adds unnecessary complexity for the current fusion framework goals.
- **Solution 3 (Chosen): Separation of Schema and Data**
  - Reasoning: Strictly adheres to the `GEMINI.md` mandate where `/src/schema` contains the schema and `/src/data` contains instances. This improves observability by clearly separating the "rules" (schema) from the "content" (data) and facilitates easier testing of multiple data instances.

## 2026-03-16 10:00 - Unified Process & Deliverables Architecture
- **Problem**: Define unified deliverables and process steps for the Fusion framework that balance AI observability with the human "Handler" role model.
- **Solution 1: Phase-based Model (Classic Lifecycle)**
  - Reasoning: Familiar and structured (like RUP/V-Modell), but risks being too rigid for AI-led orchestration.
- **Solution 2: Event-driven Model (Fluid/Agile)**
  - Reasoning: Highly flexible, but lacks the clear strategic human decision points required by the GEMINI mandate.
- **Solution 3 (Chosen): Decision-point centric Model (The "Handler" Loop)**
  - Reasoning: Re-aligns the process around the three human "Handlers" (Start, Conflicts, Exceptions), making the human-AI interaction patterns the primary structure. This directly supports the goal of human ease of interaction at critical junctures while allowing AI to handle the operational flow between decisions.

## 2026-03-15 13:00 - Unified Role System Architecture
- **Problem**: Define a unified role system that fuses RUP, V-Modell-XT, Hermes, SCRUM, and PRINCE2, emphasizing AI observability and human ease of interaction (Handlers of Start, Conflicts, and Exceptions).
- **Solution 1: Direct Accountability Mapping (The "Handler" Core)**
  - Roles: **Handler of the Start** (Strategic), **Handler of Conflicts** (Governance), **Handler of Exceptions** (Tactical), **AI Orchestrator** (Operational), **Delivery Specialist** (Technical).
  - Reasoning: Provides a clean, minimalist structure that directly implements the human-centric mandates while delegating operational complexity to AI.
- **Solution 2: Agile-Governance Hybrid (Scrum-PRINCE2 Fusion)**
  - Roles: **Product Executive** (Handler of Start), **Governance Board** (Handler of Conflicts), **Flow Guardian** (Handler of Exceptions), **AI Assistant**, **Cross-Functional Team**.
  - Reasoning: Leverages familiar terms from established frameworks but re-aligns them to the Handler model, potentially easier for legacy teams to adopt.
- **Solution 3: Functional Stream Fusion (Discipline-Oriented)**
  - Roles: **Initiator**, **Arbitrator**, **Resolver**, **AI Process Engine**, **Workstream Leads**.
  - Reasoning: Focuses on the function performed rather than the position, allowing for more flexible scaling in complex environments.
- **Decision (Chosen): Solution 1: Direct Accountability Mapping (The "Handler" Core)**
  - Reasoning: This solution most strictly adheres to the GEMINI.md mandate for human roles while providing the highest observability for AI. By naming the roles after their primary human interaction pattern, it simplifies the "Ease of Interaction" goal.

## 2026-03-16 11:00 - Unified Framework Schema Architecture
- **Problem**: Define a schema architecture for the unified framework that supports both AI observability and human-friendly YAML interaction.
- **Solution 1: Modular Schema (Per-Component)**
  - Reasoning: Splits roles, deliverables, and process steps into separate schemas. Good for isolation but complex to manage cross-component referential integrity.
- **Solution 2: Relationship-centric Schema (Graph-based)**
  - Reasoning: Focuses on the connections between elements. High AI observability but potentially difficult for human "handlers" to read and edit.
- **Solution 3 (Chosen): Monolithic JSON Schema (The Unified Core)**
  - Reasoning: Manages roles, deliverables, and process steps as a single unit in one schema. Ensures cross-component referential integrity is easily validated and provides a clear, comprehensive structure for both AI and humans.
- **Decision (Chosen): Solution 3: Monolithic JSON Schema (The Unified Core)**
  - Reasoning: This provides the best balance for maintaining a strictly typed system where deliverables can easily reference their accountable roles, and process steps can reference their outputs.

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

## 2024-03-14 14:00 - Comprehensive Specification Search Results
- **Problem**: Attempt to find more comprehensive original PDF specifications for HERMES 2022 and V-Modell-XT 2.3 to replace Wikipedia-based summaries.
- **Findings**: Extensive searching of official domains (admin.ch, bund.de) and general repositories did not yield public, direct download links to the full reference manuals in PDF format. Most official documentation is delivered via interactive web portals or restricted-access PDFs.
- **Decision**: Continue using the current high-quality Markdown conversions of comprehensive reference summaries. The SCRUM specification remains the full official guide.
- **Reasoning**: The current summaries provide sufficient detail for role, deliverable, and process definition as required by the fusion framework goal, and are more accessible for AI consumption than non-public or fragmented PDF sources.

## 2026-03-15 11:30 - Final Comprehensive Specification Verification
- **Problem**: Confirm if more comprehensive original specifications (PDFs) are available for the core frameworks as per ROADMAP.md.
- **Solution 1 (Chosen)**: Exhaustive search for official PDF manuals for RUP, PRINCE2, HERMES 2022, and V-Modell-XT 2.3.
- **Findings**: Similar to previous attempts, full official manuals for several frameworks (especially RUP and PRINCE2) are commercially restricted or not available as single public PDFs. The existing collection in `/specifications` represents the most comprehensive accessible baseline, including official PDFs for SCRUM and V-Modell-XT Bund 2.3.
- **Decision**: Finalize the specification acquisition phase and proceed with the current Markdown conversions as the foundational data for the unified framework.
- **Reasoning**: The current specifications provide sufficient depth for identifying roles, processes, and deliverables, and maintaining consistency is now prioritized over further searching for potentially unavailable documents.

## 2026-03-14 14:15 - Specification Processing Automation
- **Problem**: Implement the roadmap step to recursively check for new files, mark them as ".original.", and convert them to Markdown.
- **Solution 1**: Purely manual renaming and conversion using CLI tools.
  - Reasoning: Simple but tedious and error-prone for multiple files.
- **Solution 2 (Chosen)**: Use systematic CLI commands (find, rename, and conversion tools) to identify and process files.
  - Reasoning: Provides a good balance between automation and control, ensuring all files are correctly handled according to the naming convention and converted efficiently.
- **Solution 3**: Develop a custom Python script for the entire pipeline.
  - Reasoning: Robust and reusable, but potentially overkill for the current number of files and initial setup phase.

## 2026-03-15 12:00 - AI-Friendly Schema Format Choice
- **Problem**: Research and define the best schema format for the unified system that balances AI observability with human ease of interaction (as "handlers").
- **Solution 1**: JSON-LD (Linked Data).
  - Reasoning: Excellent for AI semantic reasoning and cross-framework linking, but potentially overwhelming for human "handlers" to manage manually.
- **Solution 2 (Chosen)**: YAML for data storage/interaction, validated by JSON Schema.
  - Reasoning: YAML provides the best balance of human readability for "handlers of the start, conflicts, and exceptions" while JSON Schema ensures the rigid structure required for AI observability and automated verification.
- **Solution 3**: Markdown with Frontmatter.
  - Reasoning: Highly readable, but less efficient for modeling complex relational data structures between roles, deliverables, and process steps compared to a dedicated data format.
