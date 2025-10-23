# COPP AHP Military Planner - Architecture Documentation

## Overview

The COPP AHP (Analytical Hierarchy Process) Military Planner is a Streamlit-based web application designed for strategic military operational planning. It implements a hierarchical decision-making framework for assessing and tracking progress across multiple forces.

## System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   Web Browser (UI)                       │
│                    localhost:8501                        │
└─────────────────────────────────────────────────────────┘
                          ↕ HTTP
┌─────────────────────────────────────────────────────────┐
│                  Streamlit Server                        │
│  ┌───────────────────────────────────────────────────┐  │
│  │                   app.py                          │  │
│  │  - UI Components & Navigation                     │  │
│  │  - Login System                                   │  │
│  │  - Dashboard & Visualization                      │  │
│  │  - Tab Management (Phases/Objectives/DPs/Tasks)   │  │
│  └───────────────────────────────────────────────────┘  │
│                          ↕                               │
│  ┌───────────────────────────────────────────────────┐  │
│  │              ahp_backend.py                       │  │
│  │  - Data Management                                │  │
│  │  - Project CRUD Operations                        │  │
│  │  - Excel Import/Export                            │  │
│  │  - Progress Calculation                           │  │
│  └───────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
                          ↕ File I/O
┌─────────────────────────────────────────────────────────┐
│              File System (JSON/Excel)                    │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │  projects/   │  │ forces.json  │  │ahp_team.json │  │
│  │  *.json      │  │              │  │              │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
```

## Core Components

### 1. Frontend (app.py)

**Purpose**: User interface and interaction layer

**Key Features**:
- **Login System**: Role-based authentication (Control vs Force users)
- **Navigation**: Sidebar with dynamic menu based on user role
- **Visualization**: Plotly charts for progress monitoring
- **Forms**: Input forms for phases, objectives, DPs, and tasks
- **Styling**: Custom CSS for military theme with tricolor elements

**Main Functions**:
- `login()`: Authentication interface
- `sidebar()`: Navigation menu
- `phases_tab()`, `objectives_tab()`, `dps_tab()`, `tasks_tab()`: Data management
- `dashboard_tab()`: Analytics and visualization
- `ko_tab()`: KO Method for task prioritization
- `control_panel_tab()`: System configuration

### 2. Backend (ahp_backend.py)

**Purpose**: Business logic and data persistence

**Key Features**:
- Project management (create, load, save, archive, delete)
- Excel import/export with flexible column mapping
- Progress calculation algorithms
- Data structure definitions

**Main Functions**:
- `load_project()`, `save_project()`: Project data persistence
- `import_excel_to_project()`: Excel file parsing and data import
- `export_project_json()`, `export_project_excel()`, `export_project_zip()`: Data export
- `compute_progress()`: Hierarchical progress calculation

### 3. Data Layer

**Structure**:
```
projects/
├── {project_name}_{force}.json    # Per-force project data
└── ...

forces.json                         # Force configuration
ahp_team.json                       # Team member credits
```

## Data Model

### Hierarchical Structure

```
Project
  └── Phases
       └── Objectives
            └── Decisive Points (DPs)
                 └── Tasks
```

### JSON Schema

**Project Data** (`projects/{name}_{force}.json`):
```json
{
  "metadata": {
    "name": "string",
    "description": "string",
    "status": "active",
    "created": "ISO8601",
    "modified": "ISO8601"
  },
  "phases": [
    {"Name": "string"}
  ],
  "objectives": [
    {"Name": "string", "Phase": "string"}
  ],
  "dps": [
    {
      "DP No": "string",
      "Name": "string",
      "Objective": "string",
      "Phase": "string",
      "Weight": "number",
      "Force Group": "string"
    }
  ],
  "tasks": [
    {
      "Task No": "string",
      "Name": "string",
      "DP No": "string",
      "Type": "T|I",
      "Weight": "number",
      "Progress": "number",
      "Intangible": "nil|partial|complete",
      "Criteria": "string",
      "Force Group": "string"
    }
  ],
  "ko": {},
  "progress": {},
  "control": {}
}
```

**Forces Configuration** (`forces.json`):
```json
["blue", "red", "yellow", "green", ...]
```

**Team Data** (`ahp_team.json`):
```json
[
  {"name": "string", "role": "string"},
  ...
]
```

## Key Algorithms

### 1. Progress Calculation

**Hierarchical Bottom-Up Approach**:

```python
Task Progress → DP Progress → Objective Progress → Phase Progress
```

1. **Task Progress**: Direct input (0-100%) with intangible adjustments
2. **DP Progress**: Average of all tasks in the DP
3. **Objective Progress**: Average of all DPs in the objective
4. **Phase Progress**: Average of all objectives in the phase

**Intangible Adjustments**:
- `nil`: Use actual achieved %
- `partial`: Max(achieved%, 50%)
- `complete`: 100%

### 2. KO Method (Pairwise Comparison)

**Purpose**: Determine relative importance of tasks within a DP

**Process**:
1. Present all pairs of tasks: (n choose 2) comparisons
2. User selects more important task for each pair
3. Score accumulation: Winner gets +1 point
4. Weight calculation: (task_score / total_score) × 100%

### 3. RAG Status Calculation

**Red-Amber-Green Indicators**:
- **Red**: Progress < red_threshold (default 40%)
- **Amber**: red_threshold ≤ Progress < amber_threshold (default 70%)
- **Green**: Progress ≥ amber_threshold

## Security Model

### Authentication
- **PIN-based**: Simple PIN authentication per role
- **Session State**: Streamlit session state for login persistence
- **Role-based Access**:
  - Control: Full access to all features
  - Force: Access to own force data only

### Data Isolation
- Each force has separate JSON files
- Control can view/modify all forces
- Forces can only access their own data

## User Roles

### Control User
**Access**: System-wide operations
- Force management (add/remove forces)
- Global progress monitoring
- RAG threshold configuration
- PIN management for all forces
- Data import/export for all forces

### Force User
**Access**: Force-specific operations
- Manage own phases, objectives, DPs, tasks
- KO Method for task prioritization
- View own force analytics
- Limited to assigned force data

## Technology Stack

### Core Technologies
- **Python 3.8+**: Programming language
- **Streamlit 1.28.0**: Web framework
- **Pandas 2.1.1**: Data manipulation
- **Plotly 5.17.0**: Interactive visualizations
- **OpenPyXL 3.1.2**: Excel file handling

### Design Patterns
- **MVC-like**: Separation of UI (app.py) and logic (ahp_backend.py)
- **Session State**: Streamlit session state for user context
- **File-based Storage**: JSON for simplicity and portability
- **Modular Tabs**: Separate functions for each feature

## Extensibility

### Adding New Features

1. **New Tab**: Add function in `app.py`, update `tab_options` in `sidebar()`
2. **New Data Type**: Update `DEFAULT_STRUCTURE` in `ahp_backend.py`
3. **New Force**: Use Force Manager UI or modify `forces.json`
4. **New Export Format**: Add function to `ahp_backend.py`

### Customization Points

- **Colors**: `FORCE_COLORS` dictionary in `app.py`
- **RAG Thresholds**: Control Panel → System Settings
- **Default Structure**: `DEFAULT_STRUCTURE` in `ahp_backend.py`
- **Styling**: CSS in `inject_css()` function

## Performance Considerations

- **File I/O**: Each project load/save is a file operation
- **Session State**: Data cached in memory during session
- **Large Projects**: May need optimization for 100+ tasks
- **Concurrent Users**: Not designed for multi-user concurrent editing

## Deployment Options

### Local Development
```bash
streamlit run app.py
```

### Production (Single User)
```bash
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

### Production (Multi-User - Not Recommended)
Consider deploying on Streamlit Cloud or using authentication middleware

## Future Enhancement Ideas

1. **Database Backend**: Replace JSON with SQLite/PostgreSQL
2. **Multi-user Support**: Add proper authentication and concurrent editing
3. **Audit Trail**: Track all changes with timestamps and users
4. **Advanced Analytics**: ML-based predictions and recommendations
5. **Mobile App**: Companion mobile application
6. **Real-time Collaboration**: WebSocket-based live updates
7. **REST API**: Separate API layer for integration

## Development Setup

See [QUICKSTART.md](QUICKSTART.md) for development environment setup.

## Credits

**Conceptualized by**: Capt Swaminathan  
**Software Designed by**: Cdr Kaki Rohit Raju  
**Organization**: DSSC Wellington • Naval Wing

---

*"To War With Wisdom"* 🦉
