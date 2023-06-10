# 🚀AndroGuard API v2.0 is Live 🎉

### What is AndroGuard?

[Androguard](https://github.com/androguard/androguard) is a full python tool to play with Android files.

### What is AndroGuard API?

Androguard API is a wrapper for androguard to parse the permissions of an APK submitted.

# Powered With

<a target="_blank" href="https://github.com/androguard/androguard"><img src="https://raw.githubusercontent.com/androguard/androguard/master/assets/CI/banner.png" width="20%"></a>
<a target="_blank" href="https://github.com/pallets/flask"><img src="https://flask.palletsprojects.com/en/2.2.x/_images/flask-logo.png" width="15%"></a>
<a target="_blank" href="https://www.docker.com/"><img src="https://www.docker.com/wp-content/uploads/2022/03/horizontal-logo-monochromatic-white.png" width="20%"></a>

## Getting Started

### Run with docker commands

```
docker pull gilzonme/androguard-api
docker run -p 5000:5000 gilzonme/androguard-api
```

### API Documentation

This is based on the above running commands which will run/expose the port at 5000

Request:

```
[POST] http://localhost:5000/
```

Parameters
```
file - APK file to be parsed
```

Response :

```
Array of Permissions
```

🪲 Report issues at <a href="https://www.reddit.com/r/androguardapi/" target="_blank">https://www.reddit.com/r/androguardapi/</a>