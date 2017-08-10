# MuxiH5

[![Website](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](http://h5.muxixyz.com)

> This is an era of mobile priority😂

this repo for muxi html5 automatic deployment
<hr/>

## How 2 use
### Step1:📝 Clone this repo

    $ git clone https://github.com/Muxi-Studio/muxih5.git

=> if you have copied the repository, don't forget to pull it!

### Step2:📱 Add html5 statics and template

    $ cd muxih5/h5

h5 statics&template structure example

    christmas(h5 name)
            -- static(static)
                -- img
                    - (img files)
                -- js
                    - (js files)
                -- css
                    - (css files)
            -- <h5name>_index_m.html(mobile index page)
            -- <h5name>_index_d.html(desktop index page)

### IMPORTANT: static file path: "/{h5_name}/static/xxxx"

=> h5 name can't start with a number <br/>
=> static can be omitted, if you use cdn

### Step3. 🐙 Commit and push!

    $ git add / commit / push

### Step4. 🍺 Cheers!

Once you commit, the webhook will pull your changes and automaic deployment!  <br/>

check [h5.muxixyz.com/{h5_name}]() for your awesome h5!

## License

Built with ❤️  and Muxistudio

