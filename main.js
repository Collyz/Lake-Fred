import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { Text } from 'troika-three-text';

// INSTANTIATIONS
const resize_scale = 1.3;
const scene = new THREE.Scene(0xffffff);                                                                   // SCENE
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000);        // CAMERA
const renderer = new THREE.WebGLRenderer({// RENDERER
	antialias: true,
	alpha: true,
	canvas: document.querySelector('#scene')
});                                  

// Renderer pixel ratio, size, and adding to DOM
renderer.setPixelRatio(window.devicePixelRatio)
renderer.setSize( window.innerWidth / resize_scale, window.innerHeight / resize_scale);
// Camera pos
camera.position.set(0, 30, 130);
// Scene background
scene.background = new THREE.Color(0x91B491);


// GLTF (Lake Model) import and creation
const gltfloader = new GLTFLoader();     
let lake;
gltfloader.load(
	//resource url
	"./assets/models/lake2.glb",
	//called when the resource is loaded
	function( gltf ){
		
		lake = gltf.scene;          // Store the THREE.Scene to use elsewhere
		lake.position.set(0, 0, 0);
		scene.add( gltf.scene );
	},
	// Called while loading is progressing
	function ( xhr ) {
		console.log( ( xhr.loaded / xhr.total * 100 ) + '% loaded' );
	},
	// Called when loading has errors
	function ( error ) {
		console.log( error );
	}
);

// IMAGE import and drawing onto a PLANE
// const planeGeo= new THREE.PlaneGeometry(40, 40);
// const textLoader = new THREE.TextureLoader();
// let texture = textLoader.load("./assets/images/website-qr.png");
// const planeMat = new THREE.MeshBasicMaterial({
// 	color:0xeba6f5,
// 	side: THREE.DoubleSide,
// 	map:texture
// });
// const plane1 = new THREE.Mesh(planeGeo, planeMat);
// plane1.position.set(15, 50, -30);
// scene.add(plane1);

// PLANE \ FLOOR
// const geo = new THREE.PlaneGeometry(2000, 2000, 8, 8);
// const mat = new THREE.MeshBasicMaterial({color: 0x000000, side: THREE.DoubleSide});
// var plane = new THREE.Mesh(geo, mat);
// plane.rotateX( -Math.PI / 2);
// plane.position.y = -15;
// scene.add(plane);


// TORUS
// const geometry = new THREE.TorusGeometry( 10, 3, 16, 100);                 //Defines Points, Vertices, Faces. etc
// const material = new THREE.MeshStandardMaterial( { color: 0xFF6347, wireframe: true} );     //Material for the torus
// const donut = new THREE.Mesh( geometry, material );                        //Actual mesh object that connects the geometry and gives a material look to it
//scene.add(donut);                                                          //Adding the torus to the scene

// TEXT
const text1 = new Text();
text1.text = 'Lake-Fred';
text1.fontSize = 10;
text1.position.set(-10, 20, -30);
text1.color = 0xE34234;

// const text2 = new Text();
// text2.text = 'Source Code';
// text2.fontSize = 10;
// text2.position.set(-12, 90, -30);
// text2.color = 0x6f08ff;
scene.add(text1);


// LIGHTS
const light1 = new THREE.DirectionalLight(0xffffff, 3);
const light2 = new THREE.DirectionalLight(0xffffff, 3);
const light3 = new THREE.PointLight(0xffffff, 5000);
const light4 = new THREE.PointLight(0xffffff, 5000);
light3.name = 'Point_Light_1';
light4.name = 'Point_Light_2';
// LIGHTS POSITION
light1.position.set(0, 20, 0);
light2.position.set(0, -20, 0);
light3.position.set(0, 50, 0);
light4.position.set(0, -60, 0);
// LIGHT HELPERS
const helper1 = new THREE.DirectionalLightHelper(light1);
const helper2 = new THREE.DirectionalLightHelper(light2);
const helper3 = new THREE.PointLightHelper(light3);
const helper4 = new THREE.PointLightHelper(light4);
scene.add(light3, light4);

// ORBIT CONTROLS
const controls = new OrbitControls(camera, renderer.domElement);           // Orbit controls
controls.enableDamping = true;
controls.autoRotate = true;

// RENDER/ANIMATION LOOP (Called normally 60 times per second)
function update() {
	requestAnimationFrame( update );
    //Add anything here to do stuff to box before rendering
	light3.position.x = Math.sin(Date.now() / 500) / 2 * 150;
	light4.position.x = Math.sin(Date.now() / 500) / 2 * 150;
	
	controls.update();                                                    // Update oribital controls
	renderer.render( scene, camera );                                     // Update renderer
}

// RESIZING
window.addEventListener('resize', onWindowResize, false);                 // Window event listener calls the resizing function
function onWindowResize(){
	// Changing the camera aspect ratio and renderer
	camera.aspect = window.innerWidth / window.innerHeight;
	camera.updateProjectionMatrix();
	renderer.setSize(window.innerWidth / resize_scale, window.innerHeight / resize_scale);
}

// Toggle wireframe
const button1  = document.getElementById('wireframe_toggle');
button1.addEventListener('click', function() {
    lake.traverse((o) => {
        if (o.isMesh && o.material instanceof THREE.MeshStandardMaterial) {
            if (o.material.wireframe) {
                o.material.wireframe = false;
            } else {
                o.material.wireframe = true;
            }
        }
    });
});

// Toggle lights
const button2 = document.querySelector('#light_toggle');
button2.addEventListener('click', () => {
    if(scene.getObjectByName('Point_Light_1') && scene.getObjectByName('Point_Light_2')){
		scene.remove(light3);
		scene.remove(light4);
		scene.add(light1);
		scene.add(light2);
	}else{
		scene.remove(light1);
		scene.remove(light2);
		scene.add(light3);
		scene.add(light4);
	}
});

const button3 = document.querySelector('#reset_camera');
button3.addEventListener('click', () => {
	controls.reset();
});

const checkbox1 = document.getElementById('cam_spin');
console.log(checkbox1);
checkbox1.addEventListener('click', function() {
	if(checkbox1.checked){
		controls.autoRotate = false;
	}else{
		controls.autoRotate = true;
	}
});


// Update
update();