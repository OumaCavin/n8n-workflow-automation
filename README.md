# n8n Workflow Automation Guide

A comprehensive guide to n8n workflow automation with hands-on examples and exercises for building automated workflows using triggers, logic, APIs, and AI.

## Overview

This repository contains practical exercises and workflow examples designed to help you master n8n workflow automation. Each example demonstrates key concepts and patterns that you can apply to your own automation projects.

## Getting Started

### Prerequisites

- Node.js 18.x or later
- n8n installed (self-hosted or cloud)
- Basic understanding of APIs and data flow

### Installation

1. Clone the repository:
```bash
git clone https://github.com/OumaCavin/n8n-workflow-automation.git
cd n8n-workflow-automation
```

2. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies (if any Python utilities included):
```bash
pip install -r requirements.txt
```

### Importing Workflows

1. Open n8n in your browser
2. Navigate to the Overview page
3. Click "Create Workflow" in the top-right corner
4. In the editor, open the menu and select "Import from File"
5. Choose the desired workflow JSON file from the `workflows/` directory

## Workflow Examples

### 1. Currency Exchange Workflow

**File:** `workflows/currency_exchange.json`

This workflow demonstrates:
- Form Trigger node for user input
- HTTP Request node for API calls
- Edit Fields node for data transformation
- Real-time exchange rate conversion

**To use:**
1. Import the workflow
2. Execute to open the form
3. Select base and target currencies
4. Submit to see real-time exchange rates

### 2. Currency Rates Workflow

**File:** `workflows/currency_rates.json`

A workflow that fetches live currency exchange rates from a public API.

**To use:**
1. Import the workflow
2. Add a Manual Trigger node
3. Connect the trigger to the HTTP Request node
4. Execute to see live exchange rates

### 3. Event Signup Workflow

**File:** `workflows/event_signup.json`

Captures event signups with form fields:
- Event name
- Attendee name
- Email

**To use:**
1. Import the workflow
2. Execute to open the form
3. Fill in the details
4. Submit to create a signup record

### 4. Contact Record Workflow

**File:** `workflows/contact_record.json`

Creates structured contact records with:
- Company name
- Contact name
- Email address

**To use:**
1. Create a new workflow
2. Add Manual Trigger
3. Add Edit Fields (Set) node
4. Configure fields as shown in the example

### 5. Filtered Contact Workflow

**File:** `workflows/contact_filtered.json`

Demonstrates field filtering by keeping only:
- Contact name
- Email

This is useful for systems that don't need all contact information.

### 6. Event Signup with Timestamp

**File:** `workflows/event_signup_timestamp.json`

Advanced event signup that captures:
- Event name
- Attendee name
- Email
- Submission timestamp

## Key Concepts

### Triggers

Triggers start your workflow. Common types include:
- **Manual Trigger**: Start workflow manually
- **Form Trigger**: Collect user input via form
- **Schedule Trigger**: Run at specific intervals
- **Webhook Trigger**: Start from external HTTP requests

### Nodes

Nodes process data in your workflow:

- **HTTP Request**: Call external APIs
- **Edit Fields**: Transform and filter data
- **Code**: Custom JavaScript/Python logic
- **IF**: Conditional branching

### Data Flow

1. Trigger receives input (form data, webhook, schedule)
2. Data passes through each node sequentially
3. Each node can transform, filter, or enhance data
4. Final node outputs the result

## n8n Expressions

n8n uses expressions for dynamic values:

```javascript
{{ $json.fieldName }}        // Access field
{{ $now }}                   // Current timestamp
{{ $json.price * 1.1 }}      // Calculate
{{ $binary.file.data }}      // Binary data
```

## Best Practices

1. **Start Simple**: Begin with basic workflows and add complexity gradually
2. **Use Descriptive Names**: Name nodes clearly for easy debugging
3. **Test Incrementally**: Execute after each node to catch errors early
4. **Handle Errors**: Add error handling for production workflows
5. **Document Your Work**: Add notes to complex nodes

## Public APIs Used

The examples use these free public APIs:
- Exchange rates API: `https://api.exchangerate-api.com/v4/latest/`
- Any HTTP endpoint returning JSON

## Project Structure

```
n8n-workflow-automation/
├── workflows/           # n8n workflow JSON files
├── documentation/       # Detailed guides
├── src/                 # Helper scripts
├── tests/               # Test workflows
├── .github/             # GitHub configuration
├── README.md            # This file
├── requirements.txt     # Python dependencies
└── setup.py             # Python setup
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - See LICENSE file for details.

## Author

Cavin Otieno - Software Developer and Automation Expert

## Resources

- [n8n Official Documentation](https://docs.n8n.io/)
- [n8n Community Forum](https://community.n8n.io/)
- [n8n GitHub Repository](https://github.com/n8n-io/n8n)