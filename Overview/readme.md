# Overview

## Overall Routine
|  | Allocation Routines | Deallocation Routines |  |
| --- | --- | --- | --- |
| Cpython | 74 | 31 | 105 |
| FFmpeg | 257 | 128 | 385 |
| Httpd | 101 | 36 | 137 |
| Memcached | 17 | 15 | 32 |
| OpenSSL | 79 | 56 | 135 |
| Redis | 120 | 89 | 209 |
| All | 648 | 355 | 1003 |

## Syntax
### Argument Usage
<table dir="ltr" style="table-layout:fixed;font-size:10pt;font-family:Arial;width:0px;border-collapse:collapse;border:none" cellspacing="0" cellpadding="0" border="0">
  <thead>
    <tr style="height:21px;">
      <th></th>
      <th colspan=3>Allocation</th>
      <th colspan=2>Deallocation</th>
    </tr>
  </thead><colgroup><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"></colgroup>
  <tbody>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;"></td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:center;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;AS&quot;}">AS</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:center;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;IV&quot;}">IV</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:center;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;RD&quot;}">RD</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:center;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;OD&quot;}">OD</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:center;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;RD&quot;}">RD</td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-left:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;Cpython&quot;}">Cpython</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:37}">37</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:44}">44</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:19}">19</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:6}">6</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:30}">30</td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-left:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;FFmpeg&quot;}">FFmpeg</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:58}">58</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:133}">133</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:106}">106</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:33}">33</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:109}">109</td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-left:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;Httpd&quot;}">Httpd</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:19}">19</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:68}">68</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:94}">94</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:18}">18</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:24}">24</td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-left:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;Memcached&quot;}">Memcached</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:6}">6</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:7}">7</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:7}">7</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:7}">7</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:14}">14</td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-left:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;OpenSSL&quot;}">OpenSSL</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:13}">13</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:51}">51</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:13}">13</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:14}">14</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:51}">51</td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-left:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;Redis&quot;}">Redis</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:32}">32</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:81}">81</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:35}">35</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:41}">41</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:52}">52</td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;border-left:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;All&quot;}">All</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:165}" data-sheets-formula="=SUM(R[-6]C[0]:R[-1]C[0])">165</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:384}" data-sheets-formula="=SUM(R[-6]C[0]:R[-1]C[0])">384</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:274}" data-sheets-formula="=SUM(R[-6]C[0]:R[-1]C[0])">274</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:119}" data-sheets-formula="=SUM(R[-6]C[0]:R[-1]C[0])">119</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:280}" data-sheets-formula="=SUM(R[-6]C[0]:R[-1]C[0])">280</td>
    </tr>
  </tbody>
</table>
