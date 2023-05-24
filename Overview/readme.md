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
