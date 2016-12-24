#coding: utf-8

"""
    muxih5~deploy.py
    `````````````````

    h5.muxixyz.com automatic deployment
"""

import os
import shutil

h5_path = os.path.abspath(os.path.join(os.path.dirname('__file__'), 'h5'))
deploy_path = os.path.abspath(os.path.join(os.path.dirname('__file__'), 'deploy'))
route_path = os.path.abspath(os.path.join(os.path.dirname('__file__'), 'route.py'))
app_path = os.path.abspath(os.path.join(deploy_path, 'app'))
h5_list = os.listdir(h5_path)

def register_blueprint(h5_list):
    for h5 in h5_list:
        try:
            h5_blueprint_path = os.path.abspath(
                os.path.join(deploy_path, 'app/{h5}'.format(h5=h5)))
            if not os.path.isdir(h5_blueprint_path):
                os.popen(
                    "cd {app_path} && mana blueprint {h5name}".format(
                        app_path = app_path,
                        h5name = h5))
                create_template_static(h5_blueprint_path)
            else: pass
        except:
            raise
    return

def create_template_static(path):
    os.popen("cd {path} && mkdir templates".format(path=path))
    os.popen("cd {path} && mkdir static".format(path=path))
    for sub in ['img', 'js', 'css']:
        os.popen("cd {path}/static && mkdir {sub}".format(path=path, sub=sub))

def copy_statics(h5_list, deploy_path):
    for h5 in h5_list:
        h5_static_path = os.path.join(h5_path, '{h5}/static'.format(h5=h5))
        deploy_h5_static_path = os.path.join(deploy_path, 'app/{h5}/static'.format(h5=h5))
        try:
            if os.path.isdir(deploy_h5_static_path):
                shutil.rmtree(deploy_h5_static_path)
            if os.path.isdir(h5_static_path):
                shutil.copytree(h5_static_path, deploy_h5_static_path)
            else: pass
        except:
            raise
    return 

def copy_templates(h5_list, deploy_path):
    for h5 in h5_list:
        h5_index_m = os.path.join(h5_path, '{h5}/index_m.html'.format(h5=h5))
        deploy_h5_index_m = os.path.join(deploy_path,
                'app/{h5}/templates/index_m.html'.format(h5=h5))
        h5_index_d = os.path.join(h5_path, '{h5}/index_d.html'.format(h5=h5))
        deploy_h5_index_d = os.path.join(deploy_path,
                'app/{h5}/templates/index_d.html'.format(h5=h5))
        try:
            if os.path.isdir(h5_index_m):
                shutil.copyfile(h5_index_m, deploy_h5_index_m)
            if os.path.isdir(h5_index_d):
                shutil.copyfile(h5_index_d, deploy_h5_index_d)
        except:
            raise
    return

def create_route(h5_list, deploy_path, route_path):
    route_template = route_path
    for h5 in h5_list:
        h5_route_file = os.path.join(deploy_path, 'app/{h5}/views.py'.format(h5=h5))
        with open(route_template,'r') as views_template_file:
            with open(h5_route_file, 'w+') as h5_views_file:
                for line in views_template_file:
                    newline = line.replace('{{ h5blueprint }}', '{h5}'.format(h5=h5))
                    h5_views_file.write(newline)
    return

if __name__ == '__main__':
    register_blueprint(h5_list)
    copy_statics(h5_list, deploy_path)
    copy_templates(h5_list, deploy_path)
    create_route(h5_list, deploy_path, route_path)
