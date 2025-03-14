# Solar Energy Calculator

This project is a web application that calculates the estimated solar energy output based on user input, including the city location, total area of solar panels, and their efficiency. It utilizes the Flask framework for the web interface and integrates with external APIs to fetch solar irradiance data.

## Features

- User-friendly interface for inputting solar panel specifications.
- Calculates daily energy output based on solar irradiance data.
- Displays results including latitude, longitude, solar irradiance, and estimated energy output.

## Project Structure

```
solar-energy-calculator
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── static
│   │   └── style.css
│   └── templates
│       └── index.html
├── requirements.txt
├── run.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd solar-energy-calculator
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python run.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.

3. Enter the required information in the form:
   - City where the solar panels will be located.
   - Total area of solar panels (in square meters).
   - Efficiency of solar panels (in percentage).

4. Submit the form to view the estimated daily energy output.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.