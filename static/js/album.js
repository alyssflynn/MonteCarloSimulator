
var photos = [
  {
    'src': '../static/img/Normal_gastric_mucosa_low_mag1.jpg',
    'title': 'Normal gastric mucosa',
    'desc': 'Intermediate magnification micrograph of normal gastric mucosa, i.e. inner most layer of the stomach. H&E stain.',
    'attribution': 'By <a href="//commons.wikimedia.org/wiki/User:Nephron" title="User:Nephron">Nephron</a> - <span class="int-own-work" lang="en">Own work</span>, <a href="https://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>',
    'link': 'https://commons.wikimedia.org/w/index.php?curid=10890698'
  },
  {
    'src': '../static/img/Auer_Rods_in_Leukemic_Blast.jpg',
    'title': 'Auer Rods in Leukemic Blast',
    'desc': 'This patient has apparent recurrence of treated acute myeloid leukemia after 7-year remission. Wright stain, 1000X.',
    'attribution': 'By <a rel="nofollow" class="external text" href="https://www.flickr.com/people/78147607@N00">Ed Uthman</a> from Houston, TX, USA - <a rel="nofollow" class="external text" href="https://www.flickr.com/photos/euthman/2434847298/">Auer Rods in Leukemic Blast</a>Uploaded by <a href="//commons.wikimedia.org/wiki/User:CFCF" title="User:CFCF">CFCF</a>, <a href="https://creativecommons.org/licenses/by/2.0" title="Creative Commons Attribution 2.0">CC BY 2.0</a>, <a href="">Link</a>',
    'link': 'https://commons.wikimedia.org/w/index.php?curid=30103850'
  },
  {
    'src': 'https://upload.wikimedia.org/wikipedia/commons/9/95/Nested_variant_of_urothelial_carcinoma_-_high_mag.jpg',
    'title': 'Nested variant of urothelial carcinoma - high mag',
    'desc': 'High magnification micrograph of nested variant of urothelial carcinoma, also nested urothelial carcinoma and nested variant of urothelial cell carcinoma. H&E stain.',
    'attribution': 'By <a href="//commons.wikimedia.org/wiki/User:Nephron" title="User:Nephron">Nephron</a> - <span class="int-own-work" lang="en">Own work</span>, <a href="https://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>',
    'link': 'https://commons.wikimedia.org/w/index.php?curid=17650699'
  }
];

function make_card(photo){
  var card = `<div class="col">
    <div class="card" style="width: 18rem;">
      <img class="card-img-top" src="${photo.src}" alt="${photo.title}">
      <div class="card-body">
        <h5 class="card-title">${photo.title}</h5>
        <p class="card-text">${photo.desc}</p>
        <small class="text-muted">${photo.attribution}</small>
        <a href="${photo.link}" class="btn btn-primary">See more</a>
      </div>
    </div>
  </div>`;
  return card;
};

function make_album_card(photo){
  var card = `<div class="col-md-4">
    <div class="card mb-4 box-shadow">
      <img class="card-img-top" src="${photo.src}" alt="${photo.title}" style="height: 100%; width: 100%; display: block;">
      <div class="card-body">
        <h5 class="card-title">${photo.title}</h5>
        <p class="card-text">${photo.desc}</p>
        <div class="d-flex justify-content-between align-items-center">
          <div class="btn-group">
            <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
            <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
          </div>
          <small class="text-muted">${photo.attribution}</small>
        </div>
      </div>
    </div>
  </div>`;
  return card;
};


function make_album(photos){
  var cards = photos.map(make_album_card).join('');
  var row = `<div class="row">${cards}</div>` ;
  var album = `<div class="album py-5 bg-light"><div class="container">${row}</div></div>`
  return album;
};

document.write(make_album(photos));
