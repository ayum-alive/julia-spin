import numpy as np,math,os
W,H=300,200
x=np.linspace(-1.6,1.6,W);y=np.linspace(-1.05,1.05,H)
z0=x[None,:]+1j*y[:,None]
os.makedirs('f',exist_ok=True)
for k in range(48):
    a=2*math.pi*k/48;c=0.7885*np.exp(1j*a)
    z=z0.copy();n=np.zeros(z.shape)
    for i in range(60):
        m=abs(z)<2;z[m]=z[m]**2+c;n[m]+=1
    t=n/60
    rgb=np.stack([255*t**.5,200*t,255*(1-t)**2],-1).astype(np.uint8)
    open('f/%02d.ppm'%k,'wb').write(b'P6 %d %d 255\n'%(W,H)+rgb.tobytes())
