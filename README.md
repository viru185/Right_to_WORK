![right to work](images\Right-to-work-checks.jpg)

# Right to WORK 
 It will automate the process of editing right to work editing.

- Makes is to easy to generate fake right to work.
- It supports custom inamge upload.
- Keep the same formate and text for authentic.

## Installation and usage

This web app uses the flask and run locally. You can use various hosting services to host app on the web.

 #### 1. Open the desired location in the of your fancy Terminal.
- Use [git](https://git-scm.com/downloads) virsion control system to clone repo.

```bash
git clone viru185/Right_to_WORK
```

#### 2. Create virtual environment
```bash
python -m venv .venv

.venv/scripts/activate
```

#### 3. Install requirements
- Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Requirements.

```bash
pip install -r requirements.txt
```

#### 4. Run the APP

 ```bash
.venv/Scripts/python.exe app.py
```

- It will start local server and can be access by below address which is only access by server running device.
  - http://127.0.0.1:5000

- App can be accessed on local network by finding devie ip address.
  - http://localipaddress:5000

> - password is **virenisthebest**

## Demo Images

Index page | Generated Template
---------- | ------------------
![Index][def2] | ![template][def3]

## TO-DO

- [ ] Make every click redirect to home page.
- [ ] Delete the used photo after the generating the template.
- [ ] Wrong password pop does not work.



[def1]: images\Right-to-work-checks.jpg
[def2]: images\index.png
[def3]: images\template.png