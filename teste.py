from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt  


html = """
<table>

 <tr>
   <td>nome</td>
   <td>idade</td>
 </tr>

  <tr>
   <td>MARIO</td>
   <td>30</td>
 </tr>

  <tr>
   <td>ANA</td>
   <td>25</td>
 </tr>

  <tr>
   <td>JULIA</td>
   <td>20</td>
 </tr>

</table>

"""
