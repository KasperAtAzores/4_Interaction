import bpy
from math import cos, sin, radians, pi

# https://www.vector-eps.com/wp-content/gallery/diamong-geometric-shapes-vector/thumbs/thumbs_diamong-geometric-shapes-vector5.jpg

def split_circle(N, offset=0):
    return [ radians(a+offset) for a in range(0,360, int(360/N) )]

# computes an index based on a cyclus of N, and offset
def mod(a, N,offset):
    return (a % N) + offset

def gemstone_mesh_top():
    r0 = 2
    r1 = 3
    r2 = 4
    r3 = 2
    golden_ratio = 1.618
    #h = 2.2+(2.2*golden_ratio)
    h = 6.2
    verts = [(cos(v)*r0, sin(v)*r0, h) for v in split_circle(6)]
    verts.extend( [(cos(v)*r1, sin(v)*r1, h-1) for v in split_circle(6,30)] )
    verts.extend( [(cos(v)*r2, sin(v)*r2, h-2) for v in split_circle(12)] )
    verts.extend( [(cos(v)*r2, sin(v)*r2, h-2.2) for v in split_circle(12)] )
    verts.extend( [(cos(v)*r3, sin(v)*r3, 2) for v in split_circle(6,30)] )
    verts.append( (0,0,0) )
    # top face
    faces = [[ a for a in range(0,6) ]]
    # six triangles
    faces.extend( [ [a,a+6,(a+1)%6] for a in range(0,6)] )
    # six quadrilaterals
    faces.extend( [ [mod(a+1,6,0), mod(a,6,6), mod(2*a+2, 12, 12), mod(a+1,6,6) ] for a in range(0, 6)] )
    # twelve triangles
    faces.extend( [ [mod(a,12,12), mod(a+1,12,12), mod( int(a/2),6,6)] for a in range(0,12)] )
    # twelve small rectangles - the band
    faces.extend( [ [mod(a,12,24), mod(a+1,12,24), mod(a+1,12,12), mod(a,12,12)] for a in range(0,12)] )
    # twelve rectangles below the band
    faces.extend( [ [mod(a,12,24), mod(int(a/2),6,36), mod(a+1,12,24) ] for a in range(0,12)] )
    # final six quadrilaterals
    faces.extend( [ [mod(a,6,36), 42, mod(a+1,6,36), mod(a*2+2,12,24) ] for a in range(0,6) ] )
    me = bpy.data.meshes.new('Gemstone_top_mesh')
    ob = bpy.data.objects.new('Gemstone', me)
    me.from_pydata(verts, [], faces)
    bpy.context.scene.objects.link(ob)

gemstone_mesh_top()
    