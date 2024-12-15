import glob, os
import copy

text_contact='''
    <div style="display:inline; float:right">

        <a  href="https://www.youtube.com/playlist?list=PLjNE4v_WVGw0oQcekmFl51MuG3EwAUC0g">
            <button    type="button"                
               style="
                    border: none;
                    color: white;
                    padding: 15px 32px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 16px;
                    margin: 4px 2px;
                    cursor: pointer;
                    background-color: #FF5733;
               "
               >YouTube</button>
        </a>

        &nbsp;

        <a href="mailto:physicsbootcamp1@gmail.com">
            <button    type="button"                
               style="
                    border: none;
                    color: white;
                    padding: 15px 32px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 16px;
                    margin: 4px 2px;
                    cursor: pointer;
                    background-color: #4CAF90;
               "
               >Contact</button></a>

        &nbsp;
        <a href="http://www.physicsbootcamp.org/iit"> 
            <button    type="button"                
               style="
                    border: none;
                    color: white;
                    padding: 15px 32px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 16px;
                    margin: 4px 2px;
                    cursor: pointer;
                    background-color: #2FAF70;
               "
               >Contests</button>
        </a>  


    </div>

'''

text_paypal='''
    <div style="display:inline; float:right">
 
            <form action="https://www.paypal.com/donate" method="post" target="_top">
                <input type="hidden" name="hosted_button_id" value="66RE499VVJTSQ" />
                <input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button" />
                <img alt="" src="https://www.paypal.com/en_US/i/scr/pixel.gif" width="1" height="1" />
            </form>
    </div>
'''


import shutil

import os,glob
folder_path = './output/web/'
for filename in glob.glob(os.path.join(folder_path, '*.html')):
    os.rename(filename, filename+"~")
    destination = open(filename, "w")
    source = open(filename+"~", "r")
    for line in source:
        destination.write(line)
        if '<header id="ptx-masthead"' in line:
            destination.write(text_contact+"\n"+text_paypal+"\n")
            #destination.write(text_contact+"\n")
    source.close()
    destination.close()

