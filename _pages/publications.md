---
layout: archive
title: "PUBLICATIONS"
permalink: /PUBLICATIONS/
author_profile: true
---

1.  Liu, J.*, Dou, X. Y.*, Chen, C. Y. \*, Chen, C., Liu, C., Xu, M. M., Zhao, S. Q., Shen, B., Gao, Y. W., Han, D. L., He, C. N6-methyladenosine of chromosome-associated regulatory RNA regulates chromatin state and transcription. Science 2020, 367, 580-586.
2.  Liu, J.*; Luo, G.*; Sun, J.; Men, L.; Ye, H.; He, C.; Ren, D. METTL14 is essential for beta-cell survival and insulin secretion. Biochim. Biophys. Acta Mol. Basis Dis. 2019, 1865, 2138-2148. &#x20;
3.  Liu, J.*; Harada, B. T.*; He, C. Regulation of gene expression by N6-methyladenosine in cancer. Trends Cell Biol. 2019, 29, 487-499. &#x20;
4.  Hou, J.*; Zhang, H.*; Liu, J. \*; Zhao, Z.; Wang, J.; Lu, Z.; Hu, B.; Zhou, J.; Zhao, Z.; Feng, M.; Zhang, H.; Shen, B.; Huang, X.; Sun, B.; Smyth, M.; He, C.; Xia, Q. YTHDF2 reduction fuels inflammation and vascular abnormalization in hepatocellular carcinoma. Mol. Cancer 2019, 18, 163-179.
5.  Han, D *.; Liu, J*.; Chen, C.; Dong, L.; Huang, X.; Liu, Y.; Wang, J.; Dougherty, U.; Bissonnette, B.; Shen, B.; Weichselbaum, R.; Xu, M.; He, C. Anti-tumor immunity controlled through mRNA m6A and YTHDF1 in dendritic cells. Nature, 2019, 566, 270-274.
6.  Liu, J.*; Eckert, M.*; Harada, B.*; Liu, S.*; Lu, Z.; Yu, K.; Tienda, S.; Chryplewicz, A.; Zhu, A.; Yang, Y.; Huang, J.; Chen, S.; Xu, Z.; Leng, X.; Yu, X.; Cao, J.; Zhang, Z.; Liu, J.; Lengyel, E.; He, C. m6A mRNA methylation regulates AKT activity to promote the proliferation and tumorigenicity of endometrial cancer. Nat. Cell Biol. 2018, 20, 1074-1083. &#x20;
7.  Yue, Y.*; Liu, J.*; Cui, X.*; Cao, J.*; Luo, G.; Zhang, Z.; Gao, M.; Shu, X.; Ma, H.; Wang, F.; Shen, B.; Wang, Y.; Feng, X.; He, C.; Liu, J. VIRMA mediates preferential m6A mRNA methylation in 3\`UTR and near stop codon and associates with alternative polyadenylation. Cell. Discov. 2018, 4, 10-26.

(\*co-authors contributed equally)

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
