# Unified Role System Design

This document defines the unified role system for the Fusion Skill & RACI framework, synthesizing RUP, V-Modell-XT, Hermes, SCRUM, and PRINCE2.

## Design Philosophy
The system is built for **AI observability** and **human ease of interaction**. It categorizes roles based on their interaction patterns with the project flow. Humans act as "Handlers" of critical decision points, while AI handles the operational orchestration.

## Unified Roles

### 1. Handler of the Start (Strategic)
- **Accountability**: Initializing the project, defining the vision, securing funding, and setting the "Definition of Success".
- **Human Interaction**: Decisions on "Why" and "Whether" to proceed.
- **Mapping**:
  - **Scrum**: Product Owner (Product Goal definition)
  - **PRINCE2**: Executive
  - **Hermes**: Auftraggeber
  - **RUP**: Project Manager / Business Designer
  - **V-Modell-XT**: Lenkungsausschuss / Auftraggeber

### 2. Handler of Conflicts (Governance)
- **Accountability**: Resolving priority clashes, resource competition, and stakeholder misalignments.
- **Human Interaction**: High-level mediation and value-based prioritization.
- **Mapping**:
  - **Scrum**: Product Owner (Backlog ordering) / Scrum Master (Removing impediments)
  - **PRINCE2**: Project Board (Senior User/Supplier)
  - **Hermes**: Projektsteuerung / Anwendervertreter
  - **RUP**: Project Manager / Change Control Board
  - **V-Modell-XT**: Lenkungsausschuss

### 3. Handler of Exceptions (Tactical)
- **Accountability**: Handling deviations from the plan, risk materialization, and "Out of Tolerance" events.
- **Human Interaction**: Intervention when AI-guided automation hits a boundary.
- **Mapping**:
  - **Scrum**: Scrum Master / Developers (Sprint adaptation)
  - **PRINCE2**: Project Manager (Manage by Exception)
  - **Hermes**: Projektleiter
  - **RUP**: Project Manager / Risk Manager
  - **V-Modell-XT**: Projektleiter

### 4. AI Orchestrator (Operational)
- **Accountability**: Day-to-day workflow management, progress tracking, deliverable linking, and documentation maintenance.
- **AI Focus**: High observability, automated reporting, and proactive bottleneck identification.
- **Mapping**:
  - **Scrum**: (Partially Scrum Master / Tooling)
  - **PRINCE2**: Project Support / Project Manager (Operational tasks)
  - **Hermes**: Projektunterstützung
  - **RUP**: Project Manager (Planning/Control)
  - **V-Modell-XT**: Projektleiter (Administrative part)

### 5. Delivery Specialist (Technical)
- **Accountability**: Creation of deliverables, quality assurance, and technical implementation.
- **Human/AI Collaboration**: Expert execution guided by AI-defined standards.
- **Mapping**:
  - **Scrum**: Developers
  - **PRINCE2**: Team Manager / Team Members
  - **Hermes**: Ersteller (Rollen der Ausführung)
  - **RUP**: Implementer / Tester / Architect
  - **V-Modell-XT**: Projektteamrollen

## Role-Mapping Matrix

| Unified Role | Scrum | PRINCE2 | Hermes | RUP | V-Modell-XT |
|--------------|-------|---------|--------|-----|-------------|
| **Handler of Start** | Product Owner | Executive | Auftraggeber | Project Manager | Auftraggeber |
| **Handler of Conflicts** | Product Owner | Project Board | Anwendervertreter | CCB / PM | Lenkungsausschuss |
| **Handler of Exceptions** | Scrum Master | Project Manager | Projektleiter | PM / Risk Manager | Projektleiter |
| **AI Orchestrator** | Tooling / SM | Project Support | Proj. Unterstützung | PM (Admin) | Projektleiter (Admin) |
| **Delivery Specialist** | Developers | Team Member | Ersteller | Implementer / Architect | Projektteamrollen |
