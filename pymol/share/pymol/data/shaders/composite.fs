#version 120

uniform sampler2D colorTexA;
uniform sampler2D colorTexB;
uniform float t;

varying vec2 texCoords;

void main()
{
    vec3 colA = texture2D(colorTexA, texCoords).rgb;
    vec3 colB = texture2D(colorTexB, texCoords).rgb;
    gl_FragColor = vec4(mix(colA, colB, t), 1.0);
}
