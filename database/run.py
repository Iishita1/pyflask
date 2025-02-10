from app import create_app


flaks_app = create_app()
if __name__ == '__main__':
    flaks_app.run()