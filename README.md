# Todoist to Super Productivity Task Exporter

This project offers a seamless way to export tasks from [Todoist](https://todoist.com) to [Super Productivity](https://super-productivity.com). Designed with extensibility in mind, this tool can be adapted to support additional task management services, making it a flexible solution for developers and productivity enthusiasts.

![Task Exporter](docs/assets/todoist_to_super.png)

## Features

- **Effortless Task Export**: Export tasks from Todoist to Super Productivity with ease.
- **Customizable Options**: Filter and select specific tasks or projects for export.
- **Data Integrity**: Ensures all task details, including descriptions, due dates, and priorities, are preserved.
- **Extensible Design**: Built to allow the integration of additional task management services.
- **Open Source**: Fully customizable for your specific needs.

## Why Use This Project?

The core design focuses on **flexibility** and **scalability**. While the initial implementation supports Todoist, the modular structure enables straightforward implementation of exporters for other services. Whether you're working with Asana, Trello, or custom platforms, this project can serve as a foundation for your needs.

## Prerequisites

1. Install Python (version 3.10 or higher).
2. Obtain an API token from Todoist.
3. Install dependencies listed in `requirements.txt`.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/franzudev/todoist_to_super-productivity.git
   cd todoist_to_super-productivity
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Exporter**:
   Execute the script to export tasks:
   ```bash
   python main.py --projects --labels --token YOUR_TODOIST_API_TOKEN
   ```
2. **Import into Super Productivity**:
   - The exporter will generate a JSON file compatible with Super Productivity.
   - Open Super Productivity and import the JSON file under "Settings > Import/Export > Import from file".

## Extensibility

The codebase is designed with extensibility at its core:

- **Modular Architecture**: Easily integrate additional task management services by implementing new modules.
- **Service-Agnostic Structure**: Task data is abstracted into a universal format for compatibility with various platforms.
- **Community-Friendly**: Open to contributions for new features or services.

### Example of Adding a New Service

To support a new task management service:

1. Create a new module to interact with the service's API.
2. Implement the task mapping logic to convert service-specific data into the universal format.
3. Add the new module to the exporter pipeline.

## Contributing

We welcome contributions! If you find a bug, have a feature request, or wish to add support for another service, feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/your-feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the developers of Todoist and Super Productivity for their excellent tools.
- Inspired by the need for a scalable and extensible task migration solution.
