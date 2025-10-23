# Quick Start Guide - COPP AHP Military Planner

This guide will help you get the AHP application running in minutes.

## Prerequisites

- **Python 3.8 or higher** installed on your system
- **pip** (Python package installer)
- **Web browser** (Chrome, Firefox, Edge, or Safari)

## Installation Steps

### Step 1: Clone the Repository (if not already done)

```bash
git clone https://github.com/rocky123rocky/AHP.git
cd AHP
```

### Step 2: Install Dependencies

**On Linux/Mac:**
```bash
pip3 install -r requirements.txt
```

**On Windows:**
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application

**On Linux/Mac:**
```bash
./run.sh
```

**On Windows:**
```bash
run.bat
```

**Or run manually:**
```bash
cd "Ver 6 23 Oct 25 - for CI"
streamlit run app.py
```

### Step 4: Access the Application

The application will automatically open in your default web browser at:
```
http://localhost:8501
```

If it doesn't open automatically, manually navigate to the URL above.

## First Time Login

### Default Credentials

- **Control User**
  - Role: Control
  - PIN: `9999`
  - Access: All features including force management and global settings

- **Force Users**
  - Role: Blue, Red, Yellow, etc. (depending on configured forces)
  - PIN: `0000`
  - Access: Own force data and operations

### Login Process

1. On the login screen, select your role by clicking the appropriate button
2. Enter the PIN in the password field
3. Click the "🚀 LOGIN" button
4. You'll be redirected to the main application interface

## Basic Usage Flow

### For Control Users:

1. **Force Manager** → Add or configure forces (Blue, Red, Yellow, etc.)
2. **Phases** → Define operational phases
3. **Objectives** → Create objectives linked to phases
4. **Decisive Points** → Define DPs linked to objectives
5. **Tasks** → Create tasks linked to DPs
6. **Progress Entry** → Update task progress and weights
7. **Dashboard** → View real-time analytics

### For Force Users:

1. **Phases** → View and manage your force's phases
2. **Objectives** → Manage your objectives
3. **Decisive Points** → Define and track DPs
4. **Tasks** → Manage tasks
5. **KO Method** → Use pairwise comparison for task prioritization

## Importing Data

You can import existing data from Excel files:

1. Go to **Project Management**
2. Upload Excel file for your force
3. Supported formats:
   - Single sheet with all data
   - Multiple sheets (Phases, Objectives, DPs, Tasks)

### Excel Format Example

**Single Sheet Format:**
| Phase | Objective | DP No | DP Description | Task No | Task Description | Type | Weight | Criteria |
|-------|-----------|-------|----------------|---------|------------------|------|--------|----------|
| Phase 1 | Obj A | 1 | Critical DP | 1 | Task Alpha | T | 5 | Success criteria |

## Stopping the Application

Press `Ctrl+C` in the terminal where the application is running.

## Troubleshooting

### Application Won't Start

**Error: Module not found**
```bash
pip3 install -r requirements.txt
```

**Error: Port already in use**
```bash
streamlit run app.py --server.port 8502
```

**Error: Python not found**
- Ensure Python 3.8+ is installed
- Add Python to your system PATH

### Browser Doesn't Open

Manually navigate to: `http://localhost:8501`

### Login Issues

- Verify you're using the correct default PINs
- Control PIN: `9999`
- Force PINs: `0000`

### Data Not Saving

- Check write permissions in the application directory
- Ensure `projects/` directory exists

## Next Steps

- Explore the **Control Panel** to customize RAG thresholds
- Use **Team Management** to add development team credits
- Create new projects in **Project Management**
- Export data for backup using the export features

## Support

For detailed documentation, see [README.md](README.md)

**Credits:**
- Conceptualized by: Capt Swaminathan
- Software Designed by: Cdr Kaki Rohit Raju
- Organization: DSSC Wellington • Naval Wing

**Motto:** "To War With Wisdom"
