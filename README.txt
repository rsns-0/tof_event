1. Run main.py in ADMIN MODE
2. If it doesn't work as expected, try changing setting in config/clickconfig. Change confidence value between 0.01 and 1.
3. NotFoundException is expected behavior. At that point it is user error.
4. To stop the script, move the mouse to the top left of the screen.

NOTE FOR MATUZ:
I made an architectural mistake. It is hard to debug without the values being hard coded in python since you don't have static type checking.
I am looking into creating a codegen script to generate Python objects from JSON or csv data with validation and type coercion during the process.
Could you check and find out if there are any libraries that already do this?
I am thinking Pydantic may have some features like this but I haven't read through all the documentation yet.