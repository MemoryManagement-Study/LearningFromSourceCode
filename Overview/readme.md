# Overview

## Overall MMR
|  | Allocation Routines | Deallocation Routines | All MMR |
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

## Semantic (Functionalities)
### 1. How many routines have such functionalities?
<table dir="ltr" style="table-layout:fixed;font-size:10pt;font-family:Arial;width:0px;border-collapse:collapse;border:none" cellspacing="0" cellpadding="0" border="0">
  <thead>
    <tr style="height:21px;">
      <th></th>
      <th colspan=8>Allocation</th>
      <th colspan=8>Deallocation</th>
    </tr>
  </thead><colgroup><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"></colgroup>
  <tbody>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;border-left:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;Application&quot;}">Application</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:center;" rowspan="1" colspan="2" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;CA&quot;}">CA</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:center;" rowspan="1" colspan="2" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;HF&quot;}">HF</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:center;" rowspan="1" colspan="2" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;IM&quot;}">IM</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:center;" rowspan="1" colspan="2" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;UD&quot;}">UD</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:center;" rowspan="1" colspan="2" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;CA&quot;}">CA</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:center;" rowspan="1" colspan="2" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;DO&quot;}">DO</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:center;" rowspan="1" colspan="2" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;CM&quot;}">CM</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:center;" rowspan="1" colspan="2" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;UD&quot;}">UD</td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;Cpython&quot;}">Cpython</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:50}">50</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:67.56756756756756}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-1]*100">67.57</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:40}">40</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:54.054054054054056}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-3]*100">54.05</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:36}">36</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:48.64864864864865}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-5]*100">48.65</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:20}">20</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:27.027027027027028}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-7]*100">27.03</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:15}">15</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:48.38709677419355}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-8]*100">48.39</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:16}">16</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:51.61290322580645}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-10]*100">51.61</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:1}">1</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:3.225806451612903}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-12]*100">3.23</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:11}">11</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:35.483870967741936}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-14]*100">35.48</td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;FFmpeg&quot;}">FFmpeg</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:80}">80</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:31.1284046692607}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-1]*100">31.13</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:199}">199</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:77.431906614786}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-3]*100">77.43</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:183}">183</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:71.20622568093385}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-5]*100">71.21</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:54}">54</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:21.011673151750973}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-7]*100">21.01</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:69}">69</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:53.90625}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-8]*100">53.91</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:89}">89</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:69.53125}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-10]*100">69.53</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:2}">2</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:1.5625}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-12]*100">1.56</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:50}">50</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:39.0625}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-14]*100">39.06</td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;Httpd&quot;}">Httpd</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:19}">19</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:18.81188118811881}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-1]*100">18.81</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:31}">31</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:30.693069306930692}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-3]*100">30.69</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:84}">84</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:83.16831683168317}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-5]*100">83.17</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:25}">25</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:24.752475247524753}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-7]*100">24.75</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:15}">15</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:41.66666666666667}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-8]*100">41.67</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:11}">11</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:30.555555555555557}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-10]*100">30.56</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:1}">1</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:2.7777777777777777}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-12]*100">2.78</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:16}">16</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:44.44444444444444}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-14]*100">44.44</td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;Memcached&quot;}">Memcached</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:4}">4</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:23.52941176470588}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-1]*100">23.53</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:14}">14</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:82.35294117647058}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-3]*100">82.35</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:12}">12</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:70.58823529411765}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-5]*100">70.59</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:7}">7</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:41.17647058823529}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-7]*100">41.18</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:6}">6</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:40}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-8]*100">40.00</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:5}">5</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:33.33333333333333}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-10]*100">33.33</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}">0</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-12]*100">0.00</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:8}">8</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:53.333333333333336}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-14]*100">53.33</td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;OpenSSL&quot;}">OpenSSL</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:24}">24</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:30.37974683544304}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-1]*100">30.38</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:53}">53</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:67.08860759493672}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-3]*100">67.09</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:52}">52</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:65.82278481012658}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-5]*100">65.82</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:10}">10</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:12.658227848101266}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-7]*100">12.66</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:35}">35</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:62.5}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-8]*100">62.50</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:26}">26</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:46.42857142857143}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-10]*100">46.43</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:9}">9</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:16.071428571428573}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-12]*100">16.07</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:14}">14</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:25}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-14]*100">25.00</td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;Redis&quot;}">Redis</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:24}">24</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:20}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-1]*100">20.00</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:19}">19</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:15.833333333333332}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-3]*100">15.83</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:67}">67</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:55.833333333333336}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-5]*100">55.83</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:14}">14</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:11.666666666666666}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-7]*100">11.67</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:37}">37</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:41.57303370786517}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-8]*100">41.57</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:53}">53</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:59.55056179775281}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-10]*100">59.55</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:1}">1</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:1.1235955056179776}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-12]*100">1.12</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:31}">31</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:34.831460674157306}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-14]*100">34.83</td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;Total&quot;}">Total</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:201}" data-sheets-formula="=sum(R[-6]C[0]:R[-1]C[0])">201</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:31.01851851851852}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-1]*100">31.02</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:356}" data-sheets-formula="=sum(R[-6]C[0]:R[-1]C[0])">356</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:54.93827160493827}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-3]*100">54.94</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:434}" data-sheets-formula="=sum(R[-6]C[0]:R[-1]C[0])">434</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:66.9753086419753}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-5]*100">66.98</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:130}" data-sheets-formula="=sum(R[-6]C[0]:R[-1]C[0])">130</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:20.061728395061728}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-7]*100">20.06</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:177}" data-sheets-formula="=sum(R[-6]C[0]:R[-1]C[0])">177</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:49.859154929577464}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-8]*100">49.86</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:200}" data-sheets-formula="=sum(R[-6]C[0]:R[-1]C[0])">200</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:56.33802816901409}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-10]*100">56.34</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:14}" data-sheets-formula="=sum(R[-6]C[0]:R[-1]C[0])">14</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:3.943661971830986}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-12]*100">3.94</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:130}" data-sheets-formula="=sum(R[-6]C[0]:R[-1]C[0])">130</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:36.61971830985916}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-26]C[-14]*100">36.62</td>
    </tr>
  </tbody>
</table>

### 2. How many funcitonalities a routine could have?

<table dir="ltr" style="table-layout:fixed;font-size:10pt;font-family:Arial;width:0px;border-collapse:collapse;border:none" cellspacing="0" cellpadding="0" border="0">
  <thead>
    <tr style="height:21px;">
      <th></th>
      <th colspan=10>Allocation</th>
      <th colspan=10>Deallocation</th>
    </tr>
  </thead><colgroup><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"></colgroup>
  <tbody>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-left:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;Application&quot;}">Application</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:center;" rowspan="1" colspan="2" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;0 func&quot;}">0 func</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:center;" rowspan="1" colspan="2" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;1 func&quot;}">1 func</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:center;" rowspan="1" colspan="2" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;2 func&quot;}">2 func</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:center;" rowspan="1" colspan="2" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;3 func&quot;}">3 func</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:center;" rowspan="1" colspan="2" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;4 func&quot;}">4 func</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:center;" rowspan="1" colspan="2" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;0 func&quot;}">0 func</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:center;" rowspan="1" colspan="2" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;1 func&quot;}">1 func</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:center;" rowspan="1" colspan="2" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;2 func&quot;}">2 func</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:center;" rowspan="1" colspan="2" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;3 func&quot;}">3 func</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:center;" rowspan="1" colspan="2" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;4 func&quot;}">4 func</td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-left:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;Cpython&quot;}">Cpython</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:9}">9</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:12.162162162162163}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-1]*100">12.16</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:23}">23</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:31.08108108108108}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-3]*100">31.08</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:14}">14</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:18.91891891891892}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-5]*100">18.92</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:17}">17</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:22.972972972972975}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-7]*100">22.97</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:11}">11</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:14.864864864864865}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-9]*100">14.86</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:8}">8</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:25.806451612903224}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-10]*100">25.81</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:6}">6</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:19.35483870967742}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-12]*100">19.35</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:14}">14</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:45.16129032258064}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-14]*100">45.16</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:3}">3</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:9.67741935483871}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-16]*100">9.68</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}">0</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;"></td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-left:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;FFmpeg&quot;}">FFmpeg</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:39}">39</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:15.17509727626459}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-1]*100">15.18</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:14}">14</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:5.447470817120623}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-3]*100">5.45</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:125}">125</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:48.63813229571984}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-5]*100">48.64</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:64}">64</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:24.90272373540856}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-7]*100">24.90</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:15}">15</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:5.836575875486381}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-9]*100">5.84</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:17}">17</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:13.28125}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-10]*100">13.28</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:32}">32</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:25}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-12]*100">25.00</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:59}">59</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:46.09375}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-14]*100">46.09</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:20}">20</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:15.625}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-16]*100">15.63</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}">0</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;"></td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-left:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;Httpd&quot;}">Httpd</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:18}">18</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:17.82178217821782}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-1]*100">17.82</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:8}">8</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:7.920792079207921}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-3]*100">7.92</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:32}">32</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:31.683168316831683}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-5]*100">31.68</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:17}">17</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:16.831683168316832}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-7]*100">16.83</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:4}">4</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:3.9603960396039604}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-9]*100">3.96</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:14}">14</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:38.88888888888889}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-10]*100">38.89</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:11}">11</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:30.555555555555557}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-12]*100">30.56</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:18}">18</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:50}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-14]*100">50.00</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:13}">13</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:36.11111111111111}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-16]*100">36.11</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}">0</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;"></td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-left:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;Memcached&quot;}">Memcached</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:3}">3</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:17.647058823529413}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-1]*100">17.65</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}">0</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-3]*100">0.00</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:7}">7</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:41.17647058823529}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-5]*100">41.18</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:5}">5</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:29.411764705882355}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-7]*100">29.41</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:2}">2</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:11.76470588235294}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-9]*100">11.76</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:4}">4</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:26.666666666666668}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-10]*100">26.67</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:3}">3</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:20}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-12]*100">20.00</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:8}">8</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:53.333333333333336}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-14]*100">53.33</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}">0</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-16]*100">0.00</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}">0</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;"></td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-left:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;OpenSSL&quot;}">OpenSSL</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:32}">32</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:40.50632911392405}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-1]*100">40.51</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:62}">62</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:78.48101265822784}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-3]*100">78.48</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:19}">19</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:24.050632911392405}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-5]*100">24.05</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:4}">4</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:5.063291139240507}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-7]*100">5.06</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:3}">3</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:3.79746835443038}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-9]*100">3.80</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:11}">11</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:19.642857142857142}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-10]*100">19.64</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:40}">40</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:71.42857142857143}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-12]*100">71.43</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:32}">32</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:57.14285714285714}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-14]*100">57.14</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:6}">6</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:10.714285714285714}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-16]*100">10.71</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}">0</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;"></td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-left:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;Redis&quot;}">Redis</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:6}">6</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:5}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-1]*100">5.00</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:48}">48</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:40}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-3]*100">40.00</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:34}">34</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:28.333333333333332}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-5]*100">28.33</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:9}">9</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:7.5}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-7]*100">7.50</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:4}">4</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:3.3333333333333335}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-9]*100">3.33</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:8}">8</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:8.98876404494382}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-10]*100">8.99</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:15}">15</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:16.853932584269664}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-12]*100">16.85</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:11}">11</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:12.359550561797752}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-14]*100">12.36</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:2}">2</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:2.247191011235955}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-16]*100">2.25</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}">0</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;"></td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;border-left:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;Total&quot;}">Total</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:107}" data-sheets-formula="=SUM(R[-6]C[0]:R[-1]C[0])">107</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:16.51234567901235}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-1]*100">16.51</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:155}" data-sheets-formula="=SUM(R[-6]C[0]:R[-1]C[0])">155</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:23.919753086419753}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-3]*100">23.92</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:231}" data-sheets-formula="=SUM(R[-6]C[0]:R[-1]C[0])">231</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:35.648148148148145}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-5]*100">35.65</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:116}" data-sheets-formula="=SUM(R[-6]C[0]:R[-1]C[0])">116</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:17.901234567901234}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-7]*100">17.90</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:39}" data-sheets-formula="=SUM(R[-6]C[0]:R[-1]C[0])">39</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:6.018518518518518}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-9]*100">6.02</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:62}" data-sheets-formula="=SUM(R[-6]C[0]:R[-1]C[0])">62</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:17.464788732394364}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-10]*100">17.46</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:107}" data-sheets-formula="=SUM(R[-6]C[0]:R[-1]C[0])">107</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:30.140845070422532}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-12]*100">30.14</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:142}" data-sheets-formula="=SUM(R[-6]C[0]:R[-1]C[0])">142</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:40}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-14]*100">40.00</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:44}" data-sheets-formula="=SUM(R[-6]C[0]:R[-1]C[0])">44</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;font-weight:bold;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:12.394366197183098}" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0.00&quot;,&quot;3&quot;:1}" data-sheets-formula="=R[0]C[-1]/R[-37]C[-16]*100">12.39</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}" data-sheets-formula="=SUM(R[-6]C[0]:R[-1]C[0])">0</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;"></td>
    </tr>
  </tbody>
</table>

## Correlation
### 1. Call path length between diffrent user-defined memory management routines.
<table dir="ltr" style="table-layout:fixed;font-size:10pt;font-family:Arial;width:0px;border-collapse:collapse;border:none" cellspacing="0" cellpadding="0" border="0">
  <thead>
    <tr style="height:21px;">
      <th></th>
      <th colspan=6>Allocation</th>
      <th colspan=6>Deallocation</th>
    </tr>
  </thead><colgroup><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"></colgroup>
  <tbody>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;border-left:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;Application&quot;}">Call Path Length</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}">0</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:1}">1</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:2}">2</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:3}">3</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:4}">4</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;>4&quot;}">&gt;4</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}">0</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:1}">1</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:2}">2</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:3}">3</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:4}">4</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;>4&quot;}">&gt;4</td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-left:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;Cpython&quot;}">Cpython</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:10}">10</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:9}">9</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:13}">13</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:22}">22</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:6}">6</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:14}">14</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:8}">8</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:12}">12</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:2}">2</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:2}">2</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:2}">2</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:5}">5</td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-left:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;FFmpeg&quot;}">FFmpeg</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:2}">2</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:49}">49</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:154}">154</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:32}">32</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:18}">18</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:2}">2</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:17}">17</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:32}">32</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:59}">59</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:20}">20</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}">0</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}">0</td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-left:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;Httpd&quot;}">Httpd</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:9}">9</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:77}">77</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:12}">12</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:3}">3</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}">0</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}">0</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:7}">7</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:21}">21</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:7}">7</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:1}">1</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}">0</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}">0</td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-left:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;Memcached&quot;}">Memcached</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:2}">2</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:10}">10</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:2}">2</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:2}">2</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:1}">1</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}">0</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:4}">4</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:7}">7</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:2}">2</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:1}">1</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:1}">1</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}">0</td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-left:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;OpenSSL&quot;}">OpenSSL</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:1}">1</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:6}">6</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:33}">33</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:30}">30</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:7}">7</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:2}">2</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:1}">1</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:4}">4</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:36}">36</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:10}">10</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:5}">5</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}">0</td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-left:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;Redis&quot;}">Redis</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:1}">1</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:4}">4</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:14}">14</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:46}">46</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:36}">36</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:19}">19</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:6}">6</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:7}">7</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:54}">54</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:19}">19</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:2}">2</td>
      <td style="border-right:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:1}">1</td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;border-left:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;Total&quot;}">Total</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:25}" data-sheets-formula="=SUM(R[-6]C[0]:R[-1]C[0])">25</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:155}" data-sheets-formula="=SUM(R[-6]C[0]:R[-1]C[0])">155</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:228}" data-sheets-formula="=SUM(R[-6]C[0]:R[-1]C[0])">228</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:135}" data-sheets-formula="=SUM(R[-6]C[0]:R[-1]C[0])">135</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:68}" data-sheets-formula="=SUM(R[-6]C[0]:R[-1]C[0])">68</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:37}" data-sheets-formula="=SUM(R[-6]C[0]:R[-1]C[0])">37</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:43}" data-sheets-formula="=SUM(R[-6]C[0]:R[-1]C[0])">43</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:83}" data-sheets-formula="=SUM(R[-6]C[0]:R[-1]C[0])">83</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:160}" data-sheets-formula="=SUM(R[-6]C[0]:R[-1]C[0])">160</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:53}" data-sheets-formula="=SUM(R[-6]C[0]:R[-1]C[0])">53</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:10}" data-sheets-formula="=SUM(R[-6]C[0]:R[-1]C[0])">10</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:6}" data-sheets-formula="=SUM(R[-6]C[0]:R[-1]C[0])">6</td>
    </tr>
  </tbody>
</table>

Ratio (Percentage):

<table dir="ltr" style="table-layout:fixed;font-size:10pt;font-family:Arial;width:0px;border-collapse:collapse;border:none" cellspacing="0" cellpadding="0" border="0">
  <thead>
    <tr style="height:21px;">
      <th></th>
      <th colspan=6>Allocation</th>
      <th colspan=6>Deallocation</th>
    </tr>
  </thead><colgroup><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"><col width="100"></colgroup>
  <tbody>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;border-left:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;Application&quot;}">Call Path Length<br></td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}">0</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:1}">1</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:2}">2</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:3}">3</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:4}">4</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;>4&quot;}">&gt;4</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}">0</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:1}">1</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:2}">2</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:3}">3</td>
      <td style="border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:4}">4</td>
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;>4&quot;}">&gt;4</td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-left:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;Cpython&quot;}">Cpython</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:13.513513513513514}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-14]*100">13.51351351</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:12.162162162162163}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-15]*100">12.16216216</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:17.56756756756757}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-16]*100">17.56756757</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:29.72972972972973}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-17]*100">29.72972973</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:8.108108108108109}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-18]*100">8.108108108</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:18.91891891891892}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-19]*100">18.91891892</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:25.806451612903224}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-19]*100">25.80645161</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:38.70967741935484}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-20]*100">38.70967742</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:6.451612903225806}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-21]*100">6.451612903</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:6.451612903225806}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-22]*100">6.451612903</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:6.451612903225806}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-23]*100">6.451612903</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:16.129032258064516}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-24]*100">16.12903226</td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-left:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;FFmpeg&quot;}">FFmpeg</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0.7782101167315175}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-14]*100">0.7782101167</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:19.06614785992218}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-15]*100">19.06614786</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:59.92217898832685}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-16]*100">59.92217899</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:12.45136186770428}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-17]*100">12.45136187</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:7.003891050583658}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-18]*100">7.003891051</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0.7782101167315175}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-19]*100">0.7782101167</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:13.28125}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-19]*100">13.28125</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:25}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-20]*100">25</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:46.09375}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-21]*100">46.09375</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:15.625}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-22]*100">15.625</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-23]*100">0</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-24]*100">0</td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-left:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;Httpd&quot;}">Httpd</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:8.91089108910891}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-14]*100">8.910891089</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:76.23762376237624}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-15]*100">76.23762376</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:11.881188118811881}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-16]*100">11.88118812</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:2.9702970297029703}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-17]*100">2.97029703</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-18]*100">0</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-19]*100">0</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:19.444444444444446}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-19]*100">19.44444444</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:58.333333333333336}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-20]*100">58.33333333</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:19.444444444444446}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-21]*100">19.44444444</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:2.7777777777777777}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-22]*100">2.777777778</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-23]*100">0</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-24]*100">0</td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-left:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;Memcached&quot;}">Memcached</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:11.76470588235294}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-14]*100">11.76470588</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:58.82352941176471}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-15]*100">58.82352941</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:11.76470588235294}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-16]*100">11.76470588</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:11.76470588235294}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-17]*100">11.76470588</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:5.88235294117647}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-18]*100">5.882352941</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-19]*100">0</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:26.666666666666668}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-19]*100">26.66666667</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:46.666666666666664}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-20]*100">46.66666667</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:13.333333333333334}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-21]*100">13.33333333</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:6.666666666666667}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-22]*100">6.666666667</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:6.666666666666667}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-23]*100">6.666666667</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-24]*100">0</td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-left:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;OpenSSL&quot;}">OpenSSL</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:1.2658227848101267}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-14]*100">1.265822785</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:7.59493670886076}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-15]*100">7.594936709</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:41.77215189873418}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-16]*100">41.7721519</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:37.9746835443038}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-17]*100">37.97468354</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:8.860759493670885}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-18]*100">8.860759494</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:2.5316455696202533}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-19]*100">2.53164557</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:1.7857142857142856}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-19]*100">1.785714286</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:7.142857142857142}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-20]*100">7.142857143</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:64.28571428571429}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-21]*100">64.28571429</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:17.857142857142858}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-22]*100">17.85714286</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:8.928571428571429}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-23]*100">8.928571429</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-24]*100">0</td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-left:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;Redis&quot;}">Redis</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:0.8333333333333334}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-14]*100">0.8333333333</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:3.3333333333333335}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-15]*100">3.333333333</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:11.666666666666666}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-16]*100">11.66666667</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:38.333333333333336}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-17]*100">38.33333333</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:30}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-18]*100">30</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:15.833333333333332}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-19]*100">15.83333333</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:6.741573033707865}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-19]*100">6.741573034</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:7.865168539325842}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-20]*100">7.865168539</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:60.67415730337079}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-21]*100">60.6741573</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:21.34831460674157}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-22]*100">21.34831461</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:2.247191011235955}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-23]*100">2.247191011</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:1.1235955056179776}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-24]*100">1.123595506</td>
    </tr>
    <tr style="height:21px;">
      <td style="border-right:1px solid #000000;border-bottom:1px solid #000000;border-left:1px solid #000000;overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;Total&quot;}">Total</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:3.8580246913580245}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-14]*100">3.858024691</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:23.919753086419753}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-15]*100">23.91975309</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:35.18518518518518}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-16]*100">35.18518519</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:20.833333333333336}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-17]*100">20.83333333</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:10.493827160493826}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-18]*100">10.49382716</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:5.709876543209877}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-19]*100">5.709876543</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:12.112676056338028}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-19]*100">12.11267606</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:23.380281690140844}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-20]*100">23.38028169</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:45.07042253521127}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-21]*100">45.07042254</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:14.929577464788732}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-22]*100">14.92957746</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:2.8169014084507045}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-23]*100">2.816901408</td>
      <td style="overflow:hidden;padding:0px 3px 0px 3px;vertical-align:bottom;text-align:right;" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:1.6901408450704223}" data-sheets-formula="=R[0]C[-14]/R[-56]C[-24]*100">1.690140845</td>
    </tr>
  </tbody>
</table>

## Reliability
Year from 2018 to 2022

### External
|  | Total | caught by script | manually analysis | ML-R | ML-NR | DF-R | DF-NR | Use-After-Free | UAF-NR |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CPython | 14970 | 64 | 58 | 43 | 10 | 3 | 0 | 1 | 1 |
| FFmpeg | 19583 | 93 | 92 | 79 | 1 | 10 | 0 | 1 | 1 |
| Httpd | 2777 | 8 | 8 | 5 | 0 | 1 | 0 | 1 | 1 |
| Memcached | 507 | 10 | 8 | 3 | 3 | 1 | 1 | 0 | 0 |
| OpenSSL | 11156 | 131 | 124 | 91 | 0 | 21 | 0 | 12 | 0 |
| Redis | 5003 | 82 | 59 | 53 | 2 | 3 | 0 | 1 | 0 |
| Total | 53996 | 388 | 349 | 274 | 16 | 39 | 1 | 16 | 3 |

### Internal
|  | Total - 2021 + 2022 | api related | func | sec | perf | incr | Sum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CPython | 6704 | 34 | 28 | 0 | 2 | 4 | 34 |
| FFmpeg | 8518 | 157 | 116 | 19 | 5 | 9 | 149 |
| Httpd | 886 | 5 | 1 | 0 | 0 | 0 | 1 |
| Memcached | 198 | 6 | 4 | 0 | 0 | 0 | 4 |
| OpenSSL | 4416 | 56 | 43 | 1 | 2 | 6 | 52 |
| Redis | 1544 | 113 | 63 | 5 | 16 | 5 | 89 |
| Total | 22266 | 371 | 255 | 25 | 25 | 24 | 329 |


