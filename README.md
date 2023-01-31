# finalCapstone
<p>The final capstone project at Hyperion Dev software engineering course</p>
<p><b>The prompt for this project can be seen in the file "SE T32 - Capstone Project IV - OOP.pdf"</b></p>

<h2> The goal of this project </h2>
<p>The goal of this project was to build a simple inventory management system using OOP principles in our design. Key skills shown in this project include:</p>
<ul>
<li>managing data as Object classes</li>
<li>creating functions to operate on these objects</li>
<li>having thorogh data validation for user inputs</li>
<li>Reading in and saving to external files in standardised formats</li>
<li>importing and using packages</li>
</ul>

<h2>installation</h2>
<p>For this file to function both files inventory.py and inventory.txt need to be in the same directory location.</p> 
<h3>Required Packages:</h3>
<ul>
<li>Tabulate</li>
</ul>

<h2>Instructions</h2>
<p>Following installation:
<ol>
<li>Run 'inventory.py', you will be prompted with this menu</li>
<p>
    <img src="https://user-images.githubusercontent.com/119878579/215807664-3155b5a3-3036-49b9-a540-2494f67fada7.jpg"  />
</p>
<li>Make selection 'r' to import the invetory.txt dataset</li>
<p>
    <img src="https://user-images.githubusercontent.com/119878579/215807161-4c622abf-182f-4826-9527-9610e85da9dc.jpg"  />
</p>
<li>Once the data is imported all other functions will work, select them in the menu with there respective letters</li>
<ul>
<li><b>c - Capture shoes</b></li>
<p>This requests information from the user which is validated and saved to the txt file</p>
<li><b>v - View all shoes</b></li>
<p>This Uses the tabulate package to print in the console the full inventory list</p>
<li><b>re - Re-stock lowest Qty item</b></li>
<p>This finds the lowest quantity item and prompts user do they want to change the inventory quanitity</p>
<li><b>s - Search a shoe</b></li>
<p>This searches the data for a SKU code and returns infomration on the shoe</p>
<li><b>i - See inventory value</b></li>
<p>This calculates total inventory costs per SKU and prints them out induvidually alongide each item in the inventory list using tabulate. Total Cost of goods is also calculated and printed</p>
<p>
    <img src="https://user-images.githubusercontent.com/119878579/215812982-a7af3d92-99fc-4fb9-9847-5aa7377dd337.jpg"  />
</p>
<li><b>h - See the highest Qty item</b></li>
<p>This searched for the highest quantity item and annnounces it as on sale</p>
<li><b>e - Exit</b></li>
<p>This closes the program</p>
</ol>

<h2>Credits</h2>
<ul>
<li><b>code by: </b>Tom Neilly</li>
<li><b>task prompt: </b>Hyperion Dev</li>
</ul>
