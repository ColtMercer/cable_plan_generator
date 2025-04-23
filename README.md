# Network Device Cable Plan Generator

This tool generates detailed cable plans for network device replacements, specifically designed for data center technicians performing EOL (End of Life) device replacements. This is concept code for turning a GraphQL query from Nautobot or Netboxinto a cable plan.

## Overview

The cable plan generator takes information about both the new and existing devices (from GraphQL queries) and produces a detailed, printable cable plan document that includes:

- Device information for both new and existing equipment
- Detailed interface-by-interface cabling instructions
- Spaces for recording cable labels
- A verification checklist
- Rollback procedures
- Areas for technician notes and documentation

## Prerequisites

- Python 3.6 or higher
- Jinja2 package

Install required packages:
```
pip install jinja2
```

## File Structure

- `device_info.json` - Contains the new device information (from GraphQL)
- `existing_device_info.json` - Contains the existing device information (from GraphQL)
- `cable_plan_template.j2` - Jinja2 template for the cable plan
- `generate_cable_plan.py` - Python script to generate the cable plan
- `cable_plan.txt` - Generated output file (will be created when script runs)

## Usage

1. Prepare the JSON files:
   - Update `device_info.json` with the new device information
   - Update `existing_device_info.json` with the existing device information

2. Run the generator:
```bash
python generate_cable_plan.py
```

3. The script will generate a `cable_plan.txt` file in the same directory

4. Print the generated `cable_plan.txt` file for the data center technician

## JSON File Format

The JSON files should contain device information in the following format:

```json
{
  "data": {
    "device": {
      "hostname": "device-name",
      "model": "device-model",
      "serialNumber": "serial-number",
      "interfaces": [
        {
          "name": "interface-name",
          "type": "interface-type",
          "speed": "interface-speed",
          "remoteDevice": "connected-device",
          "remoteInterface": "connected-interface",
          "description": "interface-description"
        }
      ]
    }
  }
}
```

## Output

The generated cable plan includes:
- Device identification information
- Interface-by-interface cabling details
- Spaces for recording cable labels
- A comprehensive checklist for verification
- Clear rollback procedures
- Areas for technician notes and timestamps

## Best Practices

1. Always verify the JSON data before generating the cable plan
2. Print the cable plan on paper for the technician to use as a working document
3. Keep the completed cable plan for documentation purposes
4. Use the checklist to ensure all steps are completed
5. Document any issues or special notes in the provided spaces

## Troubleshooting

If you encounter issues:

1. Verify JSON file syntax is correct
2. Ensure all required files are in the same directory
3. Check that Python and Jinja2 are properly installed
4. Verify file permissions allow reading/writing in the directory

## Support

For issues or questions, please open a GitHub issue or contact the network team.

