# COPP AHP Military Planner

Advanced Hierarchical Process (AHP) Framework for Common Operational Planning Process (COPP) - A strategic military planning application for assessing progress in Decisive Points, Objectives & Phases.

## Overview

This application provides a comprehensive AHP-based planning system for military operations with:

- **Multi-Force Management**: Support for multiple forces (Blue, Red, Yellow, etc.) with independent planning
- **Hierarchical Planning**: Phases → Objectives → Decisive Points → Tasks
- **Progress Tracking**: Real-time monitoring of task completion and strategic goals
- **KO Method**: Pairwise comparison for task weight calculation
- **RAG Status**: Red-Amber-Green indicators for operational readiness
- **Control Dashboard**: Centralized command and control interface

## Features

- 🎯 **Decisive Points Management**: Define and track critical decision points
- 📋 **Phase Planning**: Organize operations into strategic phases
- 🎖️ **Objective Tracking**: Monitor progress toward mission objectives
- ✅ **Task Management**: Detailed task tracking with weights and progress
- ⚖️ **KO Method**: Pairwise comparison for priority assessment
- 📊 **Dashboard**: Real-time visual analytics and reporting
- 🔐 **Security**: PIN-based access control for different forces
- 👥 **Team Management**: Track development team and contributors

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/rocky123rocky/AHP.git
   cd AHP
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Quick Start

Run the application using the provided script:

```bash
./run.sh
```

Or manually:

```bash
cd "Ver 6 23 Oct 25 - for CI"
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

### Default Access Credentials

- **Control PIN**: 9999
- **Force PINs**: 0000 (for all forces)

## Usage

### 1. Login
- Select your role (Control or specific Force)
- Enter the appropriate PIN
- Click LOGIN to access the system

### 2. Control Functions
Control users have access to all features:
- Force Manager: Add/remove forces
- Progress Entry: Update task progress for all forces
- Dashboard: View comprehensive analytics
- Control Panel: Configure system settings and security

### 3. Force Functions
Force users can manage their own:
- Phases, Objectives, and Decisive Points
- Tasks and progress tracking
- KO Method for task prioritization

### 4. Project Management
- Create new projects
- Import/Export data via Excel or JSON
- Archive and manage multiple operational scenarios

## File Structure

```
AHP/
├── Ver 6 23 Oct 25 - for CI/
│   ├── app.py              # Main Streamlit application
│   ├── ahp_backend.py      # Backend logic and data management
│   ├── forces.json         # Force configuration
│   ├── ahp_team.json       # Team member information
│   ├── projects/           # Project data files
│   └── archive/            # Archived projects
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Excel Import Format

The application supports importing data from Excel files with the following sheets:
- **Phases**: Phase Name
- **Objectives**: Name, Phase
- **DPs**: DP No, Name, Objective, Phase, Weight, Force Group
- **Tasks**: Task No, Name/Description, DP No, Type, Weight, Criteria, Force Group

Alternatively, use a single sheet with all columns combined.

## Technology Stack

- **Frontend**: Streamlit
- **Visualization**: Plotly
- **Data Processing**: Pandas
- **File Handling**: openpyxl, JSON

## Credits

**Conceptualized by**: Capt Swaminathan  
**Software Designed by**: Cdr Kaki Rohit Raju

**Organization**: DSSC Wellington • Naval Wing

**Motto**: "To War With Wisdom"

## License

This is a military planning application for internal use.

## Support

For issues or questions, please contact the development team through the application's Team Credits section.
