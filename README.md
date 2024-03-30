# Listfy

Listfy is a web application designed to streamline the process of apartment management and search. With a user-friendly interface, it allows users to register on the site to access the database of apartments, add new apartment listings, and search for apartments based on their preferences.

## Features

- **User Authentication**: Secure user authentication system ensures only registered users can access the site's features.
- **Apartment Search**: Users can search for apartments based on various criteria such as location, price range, amenities, etc.
- **Apartment Addition**: Registered users can add new apartment listings to the database, expanding the available options for others.
- **Database Management**: Efficiently manages apartment data using MySQL database, ensuring quick and reliable access to information.
- **FastAPI Backend**: The backend is built using FastAPI, providing a robust and efficient API for handling apartment data.
- **React Frontend**: Utilizes React for the frontend, offering a modern and responsive user interface.

## Technologies Used

- **Backend**: FastAPI
- **Frontend**: React
- **Database**: MySQL

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed on your system:

- Docker 🐋
- Docker Compose
- Python 3.9 or newer

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/kobiop/EASS-Listings.git
    cd EASS_PROJECT
    ```

2. Build and run the Docker containers:

    ```bash
    docker-compose up --build
    ```

    **Note:** If you plan to use MySQL, please not you may need to update these environment variables in your `docker-compose.yml` file if you intend to use MySQL with specific credentials.

3. Enjoy! 🏠

The Listfy application is now running and ready for use at [http://localhost:3000](http://localhost:3000).

## Running Tests

To run tests for the application, follow these steps:

1. Access the backend container:

    ```bash
    docker exec -it eass_project-backend-1 sh
    ```

2. Navigate to the tests directory:

    ```bash
    cd tests
    ```

3. Run pytest:

    ```bash
    pytest
    ```

## Adding a Video Introduction

You can watch a quick introduction to Listfy by clicking on the image below:

[![Watch the video](https://img.youtube.com/vi/YOUR_VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID_HERE)

Replace `YOUR_VIDEO_ID_HERE` with the actual ID of your video from the video hosting platform.

## Contributing

Contributions are welcome! Please feel free to submit issues, create pull requests, or suggest improvements to make Listfy even better.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Special thanks to the developers of FastAPI, React, and MySQL for their incredible tools and technologies that made this project possible.
- Hat tip to anyone whose code was used, and to the open-source community for their continuous support and inspiration.

---

Feel free to customize this README according to your project's specific details or requirements. Happy listing! 🏢
