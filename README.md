# Time

> Startup Systems Design & Engineering
>
> Fall 2016
>
> Cornell Tech

- Build a web app that prints out the number of seconds since the start of January 1st, 1970, Coordinated Universal Time (UTC). (50%)
- Acceptable formats (basically, they need to parse with `float()`):
    - Integer
    - Float
    - Scientific notation

> Hint: that start time is also called the “epoch”, and the elapsed time is known as “Unix time”.

- It only needs to display the time as of rendering, not updated in real-time. In other words, display the time using Python, not JavaScript.
- Build it using Flask.
- Deploy to Heroku.

> The site must be available at [`fc333-time.herokuapp.com`](fc333-time.herokuapp.com). In other words, the third-level domain needs to be prefixed with your NetID. (50%)

- There is no need to “submit” the assignment, since the staff already know the URL.

## Extra credit

- Implement the same app, using only the Python standard library (no Flask, etc.) (20%)
- Email Hongyi a link to the code on GitHub if/when you complete this.

```bash
$ export FLASK_APP=hello.py
$ flask run
 * Running on http://127.0.0.1:5000/
```

---

## STEPS 💩

```bash
chmod 400 TimeStartupSystemsAssignment.pem

ssh -i "TimeStartupSystemsAssignment.pem" ubuntu@ec2-35-162-71-247.us-west-2.compute.amazonaws.com



```
