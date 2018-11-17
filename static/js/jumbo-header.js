// IMPORTANT: file paths are CORRECT because they are being traversed to from the templates/ folder

var photo_1 = '../static/img/Secretory_phase_endometrium.jpg';

// Just some other options I debated
// var photo_2 = '../static/img/Mammary_analogue_secretory_carcinoma_(H&E,_high_power)-orig.jpg';
// <!-- <img src="https://upload.wikimedia.org/wikipedia/commons/9/95/Nested_variant_of_urothelial_carcinoma_-_high_mag.jpg"> -->
// <!-- <img src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Normal_gastric_mucosa_intermed_mag.jpg" alt="Histological sample of normal gastric mucosa" > -->

document.write(`
<div class='jumbotron jumbotron-fluid' style='background-image: url(${photo_1}); text-shadow: 0 .05rem .1rem rgba(0, 0, 0, .3);'>
  <div class='container'>
    <h1 class='display-4'><strong>onco</strong>bot</h1>
    <p class='lead'>A second set of eyes for analyzing histological samples.</p>
  </div>
</div>
<!-- <div class='caption'>
  <em>By <a href='//commons.wikimedia.org/w/index.php?title=User:NormanDy&amp;action=edit&amp;redlink=1' class='new' title='User:NormanDy (page does not exist)'>NormanDy</a> - <span class='int-own-work' lang='en'>Own work</span>, <a href='https://creativecommons.org/licenses/by-sa/4.0' title='Creative Commons Attribution-Share Alike 4.0'>CC BY-SA 4.0</a>, <a href='https://commons.wikimedia.org/w/index.php?curid=44757092'>Link</a></em>
</div> -->
`);
