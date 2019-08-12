import tensorflow as tf
import csv
info5 = 'pj,Ic,cS,WB,dP,3f,dk,p1,TL,Z1,Xq,jm,92,8S,tM,PE,Oh,Qq,xN,AC,ir,xO,Jy,U2,uj,Z3,pU,k9,wW,6K,xz,l1,Me,ju,f0,qd,dN,VD,u4,gE,S3,49,AF,FK,Ha,X1,9o,cG,3Y,hZ,Mk,RF,Gn,uL,Xa,Cs,A4,rg,3k,lm,oE,Hs,AV,Fj,d1,pF,n6,rF,5j,8A,yW,YI,En,OX,p2,8k,5E,gt,04,dW,3B,YH,gz,SU,MW,nK,1e,kJ,8B,fd,Mf,cO,Kf,lB,wX,Vw,g3,HL,69,Ye,Jm,FP,j0,dC,vg,Xg,y9,Zk,Fr,ot,tC,XK,qZ,6D,5I,on,Dt,cH,Xu,eJ,0z,vB,nJ,M0,K7,uM,6O,F7,DC,bG,wV,4c,qz,lp,Kv,NV,4t,GY,py,iz,PQ,3J,8w,F3,0U,t6,pG,wu,Hy,k1,0J,X8,8N,Ao,Vl,mo,Un,Pf,8R,Hf,yl,Td,pR,nm,nh,4C,WF,ei,nn,z9,AP,tm,IB,JH,ts,Ni,Rl,xP,Is,ED,KE,DS,ZX,qB,NL,3m,YJ,b6,s2,7B,eF,KG,dp,AA,Lr,g5,Y7,Zc,zX,x3,Mh,Su,xR,ng,P4,Fw,U0,3c,AJ,Zp,ax,6n,KX,LO,or,7A,Xx,U8,KK,NH,5y,2g,vp,oI,Nv,aW,h0,pk,DX,IV,uN,HP,1K,mU,gZ,Dj,iY,lF,Tr,fk,1N,0C,1H,Dz,tB,xF,G5,fT,gS,nG,aK,d8,ni,OG,4E,b2,Qk,hM,o6,Qy,BY,uW,dZ,Nb,Yz,Wt,Hk,NK,oP,8K,gy,Aw,ay,cW,OQ,3M,zq,hY,mv,UQ,aY,mj,Cb,63,XR,iv,HG,MD,2S,sA,Id,pr,xE,7D,fv,Gc,ky,i2,36,vT,Fp,Yj,Et,oH,dD,V4,Ll,nI,VR,d6,sp,mh,cs,eN,vD,Ee,zp,KJ,ab,N3,jk,Zq,MC,bD,kk,eC,2X,jx,Wp,1U,es,Rb,Rm,Ba,jv,Ag,iB,70,I7,sn,iC,iu,6l,yf,Es,WE,aD,iO,35,oq,FL,G0,Yd,V6,8V,nb,5b,v4,97,eD,2r,AW,fo,Hg,9q,I5,QJ,h1,Wl,i6,X4,rQ,Iu,DT,Gg,xJ,KZ,XT,0N,A6,s9,i7,v5,4n,CB,Cr,jn,Qg,n0,7G,iF,5B,IU,Ua,Yx,6k,R0,cT,vu,JS,3o,rT,UF,sP,MR,VO,jy,3D,aj,Iv,ci,17,hL,gx,EE,jo,C7,6s,PV,oh,2v,2b,yQ,5f,nq,7l,Ks,E9,9r,pM,ds,qu,I0,ZH,3H,6p,LD,zV,ar,RB,DR,mS,vS,M3,e7,Wk,NR,lu,Pb,02,9T,0H,b3,p6,n7,Ym,E7,7Z,9Y,5N,wQ,1w,nf,My,DA,M8,Qo,YK,rf,P0,XB,VG,37,Sc,hR,6W,3U,zu,tV,qO,CM,Fn,15,xG,je,na,wL,c2,pZ,rE,YF,5p,FM,AU,ZC,Mm,PF,if,eQ,VA,BO,IK,FV,YV,ic,cy,cf,ZR,bc,lV,lq,a8,bR,LP,g1,Ac,WM,L6,Zx,hg,FH,rA,90,ES,25,TW,QH,cb,kw,i9,ad,U1,zw,2B,f7,Am,Kb,a0,D1,yM,wk,FZ,sO,kh,zN,dU,Ay,y1,3V,no,gQ,f2,44,Lw,mx,pz,wM,hS,hV,O1,vr,Y4,V7,ow,Io,Yq,F6,Ob,5K,zK,ek,m3,6R,l3,o7,3K,jJ,iX,qe,gF,V1,9P,so,up,rG,gJ,2V,Bn,MY,mf,vE,Sv,0a,HC,P3,06,sZ,6e,Ky,yv,pO,zR,KS,CH,So,b8,2G,ks,68,Af,ud,8Q,Jt,7f,jH,Vo,yA,fK,SR,Mp,oG,Hz,VC,Zg,HX,Y1,RX,9e,vv,dH,CI,7m,OB,Zr,z7,Gb,R9,Pm,CV,cL,FE,7N,OM,kx,S6,CZ,gp,Jg,fc,ML,FF,tk,Wy,Oe,K0,iZ,Y0,9K,Ov,r3,J8,Hj,xj,sD,Tw,zv,nd,1q,wh,Ke,JG,ua,BK,y4,JR,QY,2W,VZ,gY,Nx,3C,66,kf,eM,qN,fY,r1,PS,Xl,b7,Uk,yk,KM,yS,i1,7d,SF,MJ,e0,r2,9J,XJ,Uv,bB,dh,CS,dg,Dw,oZ,cw,Jj,XY,hj,8e,v0,yF,MZ,85,qJ,uw,sV,1i,YB,xm,pN,RU,vK,8L,tE,0S,Sa,BI,QN,82,c0,FT,qV,wR,42,ET,CN,bu,3q,yq,sm,j5,zO,g6,Tx,Vv,TJ,12,kt,IQ,ZA,j1,4L,DB,h2,38,pt,kc,Ur,0i,bE,y2,y8,xQ,tZ,cY,ef,Tu,kI,dV,Lm,N0,wP,3X,bP,RN,ZT,V2,9g,G1,OT,hs,Eb,mL,4b,Zi,gN,3l,DE,io,Dd,rc,YZ,bS,wm,mg,aH,dy,xd,vw,Sw,IZ,yX,jS,n1,E1,8t,Sd,Wh,4J,WD,7c,hp,Q2,M7,Ht,Dg,lr,cM,5l,x4,Cu,Yo,fr,gw,f3,BW,Ea,Yf,2Y,Ah,lI,tO,Tm,yo,uA,Sz,Ku,78,Zh,75,DN,Qa,Fm,eE,Av,Ze,9f,gc,F2,Tn,Hv,tp,QZ,vz,7j,oa,HJ,qx,u0,px,nP,Hx,4m,7X,Cf,6h,B6,4U,op,VN,s1,GI,TO,Gl,IW,ok,yE,az,9k,cE,NA,ST,qm,oe,ZZ,e8,Kx,bq,Rq,OK,Wq,5A,uv,nA,xV,BQ,cP,lA,96,hu,lZ,lH,Cg,f4,U9,2I,TE,AD,dX,mW,kC,Do,Jh,9j,sx,8y,Tb,I1,II,sr,6f,fE,Vz,ya,NN,JB,Mw,Pa,hn,Bg,hW,l7,UN,dT,bd,x6,OW,wp,w4,w6,GW,ij,7y,co,ib,qY,A9,Mb,W1,zt,QR,5t,ak,Xp,t9,Pz,Hi,HW,d0,N9,GN,o5,k4,Wd,Wi,ao,iI,bI,Vx,0Z,tU,nC,KV,Os,lT,kr,lN,OP,Yy,cQ,UG,Iy,bY,89,Hc,EK,s8,nM,5G,10,rn,DY,go,Bo,9i,HH,J0,L5,iq,Wa,wj,tX,ox,aS,JM,nW,4o,ex,cp,ZP,wJ,0T,nQ,Ak,NQ,XD,D2,Jc,j4,v2,ZW,Tg,gL,SX,GB,7w,Mi,o1,h7,qR,ZD,jF,DO,9H,Vi,CF,H1,sC,Qc,MI,Fh,Kj,wv,FG,nS,nL,BB,jP,EB,EN,4D,bk,mR,Jb,SQ,hw,9b,K2,vR,i5,oj,JY,db,hE,QW,Ut,lc,km,7r,5k,IR,KB,O3,z6,Qi,WT,4N,OA,w2,I9,M4,re,TR,MO,Fg,b9,0g,UI,mn,XV,uK,RR,vQ,GK,pE,4Q,73,zy,zC,KC,S4,a3,2Q,vf,q3,ws,bT,9E,BU,VQ,Bk,81,sv,6A,Gw,ap,3T,Si,gf,u6,Fi,Ci,DK,Ap,uO,IJ,o3,e3,iR,cD,gO,9O,8u,3d,4X,jz,lY,CU,qD,oU,0h,ZF,cv,Zv,9M,U7,fW,7v,v9,Ce,9X,q0,VV,9m,IH,oy,CG,0u,Wc,PP,oL,sW,La,It,md,c8,ol,jB,J9,JD,BF,RL,ee,eS,We,g0,sl,qP,bn,qC,EH,N5,1s,wA,W2,hA,9c,qQ,FO,Pn,6G,pi,47,lO,qL,Jn,Ly,DP,sE,DL,cX,to,1x,Bc,6c,6d,MA,RI,R8,qG,xc,q9,rS,pY,D9,tg,KI,ct,mC,jD,KH,Zw,QQ,BN,gv,yB,Rj,WC,SG,b5,oS,TC,3N,BV,xW,rm,Eh,NF,HB,5v,G8,t3,eb,IP,ZO,EL,ZY,64,On,Ep,Ki,32,Oq,28,Qp,6P,99,rP,Bs,FN,YW,m0,Ys,hB,l6,n2,Lp,NB,Uq,uH,1t,2C,JA,yH,2u,c6,UU,uE,jI,EP,rK,x1,Kn,6Q,eg,A7,u7,xB,Aa,I8,Dc,cq,vq,SV,j3,GV,Nh,Lj,A1,Er,As,Ux,kY,VP,h5,Lq,C8,0X,fg,bv,Xb,ER,WS,Jr,ri,YM,EQ,WA,kS,Pp,od,1Y,1B,Ya,oB,Y2,9v,5g,dl,4A,mA,55,dS,pD,t7,sN,6H,oz,4p,Ax,nN,YT,li,YD,yV,T6,pI,wC,bg,Mn,eX,HM,Sg,x7,xA,4i,8C,mX,A0,6a,sR,TP,2o,LU,wo,1f,c7,sI,cV,5d,5C,1V,Wg,VT,p0,dY,d5,0t,0F,xe,bf,Ru,LF,a1,GU,rW,VE,WL,7Q,3a,L7,ed,6u,MK,23,zc,KY,9s,jq,Zu,3n,p9,1J,hD,yC,8I,3F,kK,iG,ln,ev,eA,Hu,fm,8l,Wo,jX,F4,z1,8F,Fe,5i,Cm,uC,Zj,be,ZQ,Po,aE,Op,r7,vY,kW,ZV,nw,uX,qE,w1,Il,pu,Gx,yn,dr,O2,nc,Wm,a6,20,Us,wN,GR,Ud,An,qv,n4,Xh,br,mO,ep,W6,65,jL,IO,7I,k6,le,qs,HZ,CA,6S,lP,vP,p7,lS,y3,cn,vA,52,Oa,95,iA,Nr,vL,Fu,DJ,6M,ne,IL,8O,xx,M1,uu,7z,0W,Al,1v,t8,of,lK,6i,ZJ,qn,ca,GJ,za,DI,oD,ou,hv,CK,6b,ej,aU,4z,tz,BL,eh,JN,3w,h4,cR,4I,JF,9B,zd,fh,SW,By,0k,nD,7a,kN,eo,nZ,wB,bp,Vy,xs,p4,LK,5c,F5,fZ,Co,CW,yi,sS,wY,26,aI,2q,gU,79,K4,5W,f5,Sj,P6,aV,gh,aq,xX,FX,9n,5h,mz,Ei,Dr,lR,LN,LM,Dn,2D,MQ,BD,dG,XX,lD,am,Qj,GM,JC,SP,A3,B8,lb,84,nt,ps,Ol,RV,4e,LJ,Br,iw,WY,u2,gA,GA,dw,jM,td,H8,Kr,Ch,kU,Ju,Ed,T5,Px,K3,QM,kX,N2,Ln,1n,cl,7W,qf,qA,tJ,XZ,5o,r0,2d,gs,hG,0Y,bL,Bb,6o,3P,yU,sF,C3,3A,qM,q5,LI,QS,B3,hm,qH,2i,ry,Bq,YQ,St,BA,Cn,oR,hC,HY,QL,Lb,mp,lg,M2,Az,1T,KP,Nq,Vt,Mr,wD,Zz,T2,jh,pT,CQ,kq,yT,Hr,qi,Yp,HK,C0,2N,pX,7n,1r,ul,AI,hr,8x,Eo,W9,QD,cx,kO,Xj,7L,pq,0A,7J,xY,M6,Dl,o8,W0,22,V9,G4,LY,Nz,WK,tG,Ny,Jx,IY,au,MH,fV,oC,lj,Eq,xo,Vb,wz,u3,0j,RO,jK,AH,eY,bK,SD,nR,qa,y5,DH,PJ,5T,bx,ve,lE,z2,eP,mQ,gW,Ph,O7,KQ,oi,GS,r8,HE,yN,cr,hb,tl,V3,w7,71,va,NX,3R,UX,Pj,dt,c9,k3,pm,d7,TN,sj,8o,IM,NZ,Bf,1u,0r,R4,zl,EM,E5,mi,Ab,Tt,Ri,5s,qb,xk,Od,js,Sk,98,x9,Yt,1R,hk,bH,5V,3W,Ia,p5,H6,5m,AE,3G,PT,CO,B9,wt,vU,Zb,kV,oQ,Dx,0D,LX,rO,yG,3r,Um,2c,2H,s4,DV,CE,ZE,mT,8P,xa,iP,QT,SM,nO,ZB,Ew,oA,Kg,L0,Vk,by,Gv,Pi,mI,Be,JZ,X5,CR,Cz,RW,Ik,8g,4j,PL,Ot,HV,JP,fD,pg,SB,ph,u5,vZ,jp,rx,LS,1G,Kl,Wx,MM,H3,XL,g2,un,Gm,z0,Ko,aM,j6,us,aC,rv,ec,3s,l5,v3,Zo,J3,pP,rN,7H,Bz,8Z,uz,zx,e5,fx,wF,DU,Bt,cd,1W,UT,mZ,Bx,tH,gb,mu,9u,da,D0,hT,Bu,tu,TQ,s6,2P,zS,Sq,YE,Cc,NS,LQ,6U,Pu,DZ,rR,q4,id,FD,P2,oc,SK,G2,fH,m8,E6,mm,sX,UA,8U,rl,Zn,D8,fS,LT,0d,0P,2z,PA,tF,Ex,Qv,vj,PY,AO,yx,Gq,SL,ge,C9,W3,FU,1I,Hd,ho,Yi,Z2,Go,iy,sw,GG,TV,ZI,UE,fy,QA,NJ,Ds,KW,Xy,fU,dJ,FB,Qw,5r,K9,FW,hO,5O,xu,bA,CC,aT,Qm,tS,Js,KF,Dp,Uu,0V,KU,uR,6J,k2,He,ra,dc,RQ,sf,vW,Qd,G9,0E,bO,PC,EX,Qs,4K,UY,pb,1O,zD,JI,K1,V8,uQ,QF,9L,Nf,ae,wK,Kq,ui,ye,fF,KD,Aq,EF,sa,gK,Dv,1Z,Uh,ME,EC,vk,83,fw,PZ,fG,4a,Yw,Pg,Rr,Oi,uk,sq,aA,eq,v8,ml,EW,Hm,kz,3L,aN,zr,ww,Cl,v7,72,k8,KR,UM,Ok,Du,6E,bb,30,uh,fa,tR,YX,AR,6r,hJ,jc,Ue,oT,Nk,Xs,K8,Nu,pC,7e,oM,39,yI,7R,pp,JJ,aX,I3,mw,jZ,6V,zg,Rg,CL,qW,bF,ck,aO,T1,Q6,em,Jl,L4,AY,HU,T3,X9,ah,9C,CP,fb,91,21,vN,Ip,Hb,JT,cm,mF,2a,n8,8z,Ms,Hp,x2,60,GF,W5,bt,0w,og,34,HN,wO,AN,yP,AQ,9a,zk,Yr,33,IC,Tf,mc,Xc,cg,xD,uc,B2,8X,Ad,05,aZ,M5,9I,rh,xH,sd,In,vl,eO,45,c5,lk,m9,0n,3Q,Fq,1L,wn,F1,AZ,8m,hd,t0,ll,4W,3v,zH,74,du,aQ,TH,yd,z3,2m,GP,jG,Ig,UV,Z6,Kt,wf,F0,Wj,BT,l9,D4,6C,PM,13,Lz,tq,vI,mN,P1,kF,Nc,eG,hc,S8,xp,ze,fn,dQ,BX,T4,bQ,bZ,B0,pV,Ma,Wu,Kk,7U,Ve,W4,QP,rX,yw,G6,MT,1d,Ef,QE,ue,Qb,Qx,pS,3p,tx,YP,LV,OE,iT,DG,8q,mY,YO,62,p3,uD,7O,IA,Jw,aG,kl,Gs,LE,Sx,1D,eH,vm,Bh,OZ,we,0f,O8,oF,j9,ny,g4,Gp,mr,1C,7M,SY,kL,SH,yZ,NI,3b,4k,uB,it,lJ,NW,Bi,0l,g7,ia,8b,J7,yp,lo,Uc,dR,ke,xM,vn,QU,8D,FI,kM,3Z,CX,Of,gX,AT,LA,jl,fO,9N,Gr,t5,iM,Ga,XE,mB,lX,RT,NY,FC,MG,5Q,87,uF,Gh,Jq,I6,pw,Hq,kE,XO,YU,Z5,yy,SS,5U,YN,0o,Rn,de,14,Hw,8p,Gu,xl,yR,Xt,Di,zA,eL,YY,eT,oV,PB,AX,Ow,CD,TU,T8,3h,Vr,Ug,M9,ls,iD,fe,u9,av,Sl,11,5u,zI,n9,9W,hl,Mj,at,Ww,Ls,nF,h6,2w,x5,VK,lv,L9,kn,X2,vF,oO,PX,si,zf,Re,qc,6L,zo,ZG,pH,bV,2h,dK,gM,oo,YC,9R,wI,Vj,Yk,iE,VW,J4,Xd,GD,qt,1b,ty,WG,Q8,jR,YL,Tq,Mq,Va,Py,nx,z8,jE,sQ,6y,l8,KL,bW,Jv,uT,XA,NE,0L,O0,ov,T0,O9,CT,Q9,Ge,J5,zF,Bd,Wz,7E,Ne,eU,7o,yz,lt,Mu,Ae,tP,rJ,Yg,Zy,8Y,E4,5z,oY,Ml,1E,J1,ey,k0,tT,QI,LL,dd,uP,qK,If,8d,xb,B5,zm,NG,Lt,NT,4B,VI,yj,0K,UC,tr,vd,im,eB,aR,LH,Wr,tc,mG,46,HA,w5,pA,Y5,4Y,VH,HS,Au,R3,iQ,jg,tw,h9,5H,yh,pJ,fQ,4O,rZ,hI,Da,sM,XQ,lL,kD,Pw,Nj,IF,Jp,Eu,yg,9V,HF,No,5P,TF,Vf,xT,RZ,gG,0x,w3,gT,fR,lf,RS,mJ,3E,j8,jj,pv,Ib,Qr,1h,Xf,bj,7i,vt,3j,i3,3S,nl,7s,dx,kH,VY,XN,zJ,ko,jQ,vs,tI,bh,SZ,zE,pd,WJ,qj,xi,XF,3t,48,iK,yu,0I,jb,d4,pc,nz,AM,rY,Up,iN,ft,Fy,31,Bv,cB,OI,Gk,Lx,9z,o0,X3,dE,GQ,ga,4R,Zs,Fc,Tv,Pt,xw,eI,CY,en,A8,uZ,6N,3u,6I,TK,WU,uJ,yD,RD,mD,rt,hz,EZ,2Z,w0,cF,Uw,VS,PO,gH,FS,C6,hK,sU,xL,Nl,18,l2,E2,os,Kd,6j,WR,y7,hi,Db,07,CJ,Je,Ir,8W,p8,vM,cN,fA,bU,9t,0B,zT,a7,nB,vx,To,4S,Rs,m7,XI,8c,MF,XU,EG,ZM,mk,b1,R5,xq,Xn,53,Z4,NO,EU,L1,D7,DQ,Oz,ku,di,4v,qp,BC,Wb,KT,as,Rd,dL,FR,N7,BG,4y,jN,cU,1k,nU,4Z,Xo,I2,5X,tL,wZ,hh,VM,Sm,ux,8M,0s,a9,Fa,ZU,0v,UP,HI,UZ,7T,Fb,kQ,gV,e9,ld,oX,Y8,6w,xS,Md,OU,ns,OD,nV,hQ,Fd,xK,b0,tf,ip,af,Ul,7V,Xr,fP,Rz,VJ,1j,hH,1y,rV,y0,NM,0q,Qn,jY,cZ,Wn,ob,UK,Em,U6,1m,VB,7x,N8,7q,Kp,cI,Uj,ql,1g,pn,L2,JO,RJ,0O,4G,4F,Cx,Kc,QO,Pr,gr,Ft,cj,ut,i4,fB,Mo,d2,0M,Vq,mt,g8,7C,i8,OO,f9,j2,RA,zs,D3,5q,Rf,um,Y9,ha,QC,gd,Fo,KA,ma,nk,xh,uf,d3,Uz,Lv,2O,C1,ym,9l,Ts,S5,9d,XC,qo,67,zW,Gt,dv,gu,qS,n3,L8,lU,GT,yL,U4,7u,in,qg,Dk,fX,SJ,rp,OH,6m,Ar,he,Jf,RK,9G,tn,Nd,rM,9x,JE,OJ,iW,B1,5D,vc,oW,GO,EV,Dq,5e,th,m5,rb,LZ,qT,Ez,WO,cu,Lc,er,1Q,Eg,IT,wH,09,TX,LG,wr,sy,Wf,2p,VL,hN,g9,df,O4,Ro,94,k7,pQ,kB,sG,vy,6B,LB,ly,Tk,Gj,xZ,Ix,oK,TS,Ii,OS,59,Sr,Aj,mP,q8,MU,WZ,WX,3e,E8,Xi,4l,Rc,qU,ub,Dm,dz,IS,BP,jU,2s,Pe,kT,u8,6Z,TD,X7,bX,J6,6X,VX,sk,3x,G3,iS,AK,e2,2E,3y,r4,yJ,ag,5J,ur,vO,Ws,Yb,01,Q1,1A,0G,f8,tt,Qu,UW,Li,hx,Q4,8a,Cp,hU,gB,iL,KO,kp,Ja,Tj,Gf,ug,VU,fN,8j,GC,qh,rj,bo,N4,BZ,zQ,FJ,Uo,Np,gk,d9,AS,QV,76,q1,Te,gl,MV,AG,SO,P7,RH,vh,YR,61,Ej,Hl,cC,mE,ZL,GL,7p,3i,Sf,rH,4P,wT,kg,aF,bw,WP,24,xt,NU,tD,2K,qk,qr,O6,Oc,1a,OF,6t,ki,rq,8n,m4,2f,Qe,1o,te,0Q,DW,wc,N6,8J,j7,ON,0p,9Q,jO,Lh,Jk,lw,7b,OY,se,Z8,sh,9S,7Y,Yl,Kh,Qf,G7,kv,ru,Vm,8i,1c,Q5,PI,Uy,eu,ht,tK,lW,Ey,Yh,h8,Lg,kZ,kb,sJ,Tl,pa,Xe,hf,tY,qw,6v,U3,Ff,zP,cK,Cq,gR,uq,Qz,Ql,YG,fq,bm,dj,Bl,lx,Yc,fI,pe,t4,Ih,xC,Ty,jC,wg,tN,zG,LR,3z,Cv,m6,Tz,80,nY,hy,H9,Q0,Iz,a5,pK,PR,I4,6z,GH,Yu,Se,19,6Y,mH,b4,FQ,P5,rr,QX,ta,Rv,y6,zj,uy,56,nv,4T,cA,2k,Hh,Fk,e4,IG,xy,WQ,BR,Pq,O5,Bw,Ng,n5,UB,8v,4q,Y6,DM,Ij,Gy,k5,kA,Cd,5w,la,PH,7g,2J,Nn,ig,UR,Gz,UL,Xm,SI,BH,sB,rI,6g,Za,w8,H7,xU,Bp,wi,mM,ix,TZ,3I,dF,lC,do,Sp,6T,ys,cc,TG,Mv,rB,aw,5F,TA,Ai,s5,S9,2U,yY,00,lM,l0,PG,Mx,o4,sg,BE,Vu,pB,vV,1F,Dy,lh,Wv,W7,wb,4u,D6,nr,nE,Tc,7k,bM,TY,5Z,Pv,AB,fl,zL,HR,N1,A2,9w,ie,S1,R2,Mt,bN,Ps,ff,SE,t2,tA,pf,T9,oN,is,ID,fz,Ho,8s,fM,8r,xg,nj,58,DD,wS,ih,H0,RE,Xk,Xw,BM,K6,R6,u1,ss,Qt,F8,PK,Og,EY,NC,z4,bs,TB,MB,Om,Im,aP,Yv,Z9,z5,41,0e,zY,Vs,vb,rU,Ta,XS,WW,i0,LC,t1,FY,C2,Iw,zB,El,Ss,7S,gg,zb,4g,rD,RP,Or,6q,6F,AL,Ui,EA,0b,4V,o9,ZK,c3,rw,WI,mq,w9,Lf,Ox,wd,4s,sc,xn,ik,wa,kd,qX,f1,uI,Jd,54,fi,2n,2j,2R,jV,Th,SN,aL,Ct,Zd,4w,Jo,RC,1z,tb,ka,XP,cJ,At,dq,PD,XH,aa,0m,MS,wl,Sb,HD,BJ,vX,sT,uS,Cj,wU,S0,sL,rd,Lu,H2,5L,D5,Fl,Ck,Z0,rC,WH,5x,Vp,hX,W8,jf,gj,mV,RM,h3,ii,5R,Ek,uo,57,Bm,an,nH,A5,NP,4r,T7,5Y,Bj,JK,Qh,s3,US,C4,Cy,Zl,bC,Ca,P8,sH,EO,EJ,Uf,TI,K5,nu,yr,XW,Mz,3g,Rt,Q3,sz,Jz,Vc,ji,rk,v6,Rx,l4,gI,2T,ew,Lk,HQ,4M,P9,gm,9D,Xz,Mg,rL,2L,gi,Vg,uU,08,vG,zi,Oo,sb,cz,1S,a2,a4,bJ,zz,fp,4h,R1,bl,Pl,OR,Pc,L3,vi,FA,8T,BS,pl,IN,Ry,mK,gD,9F,Sh,QK,q6,88,6x,XM,ce,V5,mb,JV,Hn,PU,03,Cw,2A,Zm,HT,SC,7P,Z7,e6,OL,f6,dm,lG,ja,2M,X0,JQ,8G,Fs,ti,8H,s7,al,Df,B7,4f,JW,kP,Vh,rs,Ji,m1,zM,Tp,eZ,q7,1M,ea,iV,pW,lQ,v1,9y,Kw,Zf,De,lz,86,uV,qI,3O,RY,sK,5a,B4,rz,UO,YS,LW,RG,Rw,XG,Kz,pL,8h,OC,fu,gC,jr,vJ,Fv,Rh,X6,1P,F9,WN,jw,uY,hP,bz,c4,Oj,Ec,yt,2y,40,Le,il,Lo,2e,GX,fs,Y3,jT,Xv,93,x0,9A,27,1X,1p,77,tv,fC,dI,dO,S2,DF,qF,EI,my,7h,C5,Gd,8f,r6,wG,oJ,Km,gn,r5,eW,Oy,5M,kG,GE,xv,et,Nm,yO,MP,uG,vC,fJ,Nw,Pd,TT,4d,UD,U5,2t,sY,xr,iH,c1,jd,JL,zn,Ie,Ns,zU,yc,wx,po,7F,iJ,Ev,HO,tW,50,Fx,1l,Vd,ro,wq,r9,dn,dM,Rk,9U,5n,43,e1,Pk,QG,E0,ai,Rp,Gi,aJ,vo,WV,4x,zZ,su,wE,xI,Mc,bi,9Z,fL,PN,5S,om,Q7,ND,IX,ch,m2,2F,51,el,ez,YA,Ka,TM,zh,Na,gP,29,VF,hF,Sy,S7,eV,Vn,Fz,R7,2x,Ld,H4,tj,np,E3,16,yK,gq,qq,0y,dA,8E,Ti,ZS,jW,hq,0R,Ub,Dh,MN,kj,xf,SA,nX,UH,ac,q2,JU,eK,nT,aB,jt,Zt,dB,Iq,wy,PW,s0,GZ,jA,MX,eR,Sn,V0,st,qy,tQ,Nt,yb,OV,0c,QB,7t,9p,iU,4H,me,7K,UJ,JX,2l,fj,H5,ba,Yn,IE,ms,o2,Ou,x8,9h,vH,Ra,kR,ZN,J2,KN'

def save():
    tfrecords = info5.split(',')
    with open('video_trainInfo.csv','a+') as c:
        for tfrecord in tfrecords:
            vid_lvl_record = 'gs://youtube8m-ml-us-east1/2/video/train/train%s.tfrecord'%(tfrecord)
            for example in tf.python_io.tf_record_iterator(vid_lvl_record):
                tf_example = tf.train.Example.FromString(example)
                sub_vid_id = tf_example.features.feature['id'].bytes_list.value[0].decode(encoding='UTF-8')
                sub_label = tf_example.features.feature['labels'].int64_list.value
                csv_writer = csv.writer(c)
                csv_writer.writerow([sub_vid_id,sub_label])

if __name__ == '__main__':
    save()