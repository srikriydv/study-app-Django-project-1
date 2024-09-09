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


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [srikri5462ydv@gmai.com](mailto:srikri5462ydv@gmai.com).
