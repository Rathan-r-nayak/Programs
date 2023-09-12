a=open("p35(lorem txt file).txt","r+")
a.write("""------------------------------------------------------------------------------------/1
Lorem ipsum, dolor sit amet consectetur adipisicing elit. Porro, distinctio, consequuntur iusto//2
voluptatibus mollitia voluptates praesentium accusamus repellat corrupti molestias sed sint reiciendis///3
architecto tempora. Unde vel provident commodi dignissimos.////4
Lorem ipsum dolor sit amet consectetur adipisicing elit. Ad dolore debitis,/////5
molestiae consectetur rem corrupti! Non id recusandae unde illum! Eveniet,//////6
voluptatibus veritatis! Natus dignissimos nulla itaque saepe quas tempore amet///////7
at voluptatibus hic maxime consectetur repudiandae reprehenderit nemo,////////8
autem doloremque. Cupiditate, alias beatae./////////9
------------------------------------------------------------------------------------------------//////////10""")
print(a.readline())
print(a.readline())
print(a.readline())
print(a.tell())
print(a.readline())
print(a.seek(0))
print(a.readline())
print(a.readline())
print(a.readline())
print(a.tell())
a.close()