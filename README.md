# Django Study App

A Django application designed to help users study and manage their learning materials. This app includes features such as creating and managing study notes, tracking progress, and more.

## Features

- **User Authentication**: Sign up, log in, and manage user accounts.
- **Room Functionality**: Can Join any room and can have public chat
- **Messages**: Registred user can message to the room they joined and can see the all the recent messages in that particular room
- **Search** : user can search for specific room and messsages:

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/srikriydv/study-app-Django-project-1.git
   cd study-app-Django-project-1
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**:

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

   The application will be available at `http://127.0.0.1:8000/`.

## Usage

- **Access the app**: Open your web browser and go to `http://127.0.0.1:8000/`.
- **Admin Interface**: Access the admin interface at `http://127.0.0.1:8000/admin/` to manage users and study materials.

## Screenshots

Below are some screenshots of the Photo Simple App:


### Home Page
![Home](https://github.com/user-attachments/assets/6276f6c8-0256-4f8f-8ca6-ede2e79a193f)

### Login Page
![login](https://github.com/user-attachments/assets/76d0cdb0-3a0e-4800-95d0-a28911ff2f93)

### Register Page
![register](https://github.com/user-attachments/assets/18ffa809-9396-4e82-82d4-7fc12ddc6785)

### Update Profile Page
![update Profile](https://github.com/user-attachments/assets/de12770f-95a5-4409-a3a8-719bc0824918)


### Create Room Page
![Create-room](https://github.com/user-attachments/assets/e9c286a5-f503-4c5d-ba93-2b31ff662968)

### Room Page
![room-page](https://github.com/user-attachments/assets/6479c4dc-1521-4ce7-b408-85f390b2d162)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [srikri5462ydv@gmai.com](mailto:srikri5462ydv@gmai.com).
