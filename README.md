# An Interactive Kanji Graph
Confusingly similar ideographic characters can be tricky for learners of Japanese and Chinese. This web app can help by visualising methods to compute a notion of distance between two Kanji characters, connecting those which are deemed 'close together' and thus supposedly hard to tell apart:  
<p align="center">
  <img src="https://github.com/file-acomplaint/file-acomplaint/blob/main/assets/kanjigraph_solid.gif?raw=true">
</p>
At the center, we can see the kanji we are focusing on. On the periphery, we can see its closest neighbors at a certain distance reflecting the similarity between them and the centered kanji. The peripheral kanji are also arranged roughly by how similar they are amongst themselves, with strong similarity being indicated by thicker lines. 

<h2>Calculating Distances</h2>
<p>
  We intuitively understand that some kanji are more similar than others, for example а pair like (森, 林) sharing the component 木. The data visualised here takes into account the nested component structure of the kanji, including their relative position and appearance, to assign a similarity score, using a mathematical framework called Optimal Transport. <a href="https://arxiv.org/abs/2304.02493">Here</a> is our preprint detailing the method. You can also select the Bag-of-Radicals Distance by <a href="https://psycnet.apa.org/record/2002-15293-011">Yeh and Li (2002)</a> using the fraction of shared radicals and the Stroke Edit distance by <a href="https://lars.yencken.org/papers/coling-2008.pdf">Yencken and Baldwin (2008)</a> using the number of strokes to add and remove to reach one kanji from the other.
  We also recommend our open toolkit for computing all kinds of kanji-related things in the programming language R, available <a href="https://dschuhmacher.github.io/kanjistat/">here</a>.
</p>

<h2>About</h2>
<p>
This website is brought to you by <a href="https://github.com/file-acomplaint">Lennart Finke</a> and <a href="https://dschuhm1.pages.gwdg.de/">Dominic Schuhmacher</a> from the <a href="http://www.stochastik.math.uni-goettingen.de/index.php?id=182&language=en">Spatial Stochastics</a> group at the <a href="https://www.uni-goettingen.de/en/1.html">University of Göttingen</a>. It uses <a href="https://github.com/d3/d3">d3.js</a>, licensed under <a href="https://www.isc.org/licenses/">ISC</a>, and <a href="https://github.com/jgthms/bulma">Bulma</a>, licensed under <a href="http://opensource.org/licenses/mit-license.php">MIT</a>. The website content is licensed under <a href="http://opensource.org/licenses/mit-license.php">MIT</a> and you can see the source code <a href="https://github.com/file-acomplaint/kanjidist-visualiser">here</a>.
</p>
