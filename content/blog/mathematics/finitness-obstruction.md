---
title: "Checking if a topological space can be homotopy equivalent to a finite CW complex using K-theory"
description: "Using the projective class group and Wall's finitness obstruction to determine if a space can be homotopy equivalent to a finite CW complex."
tags:
  - K-theory
  - Algebraic topology
  - Mathematics
date: "2026-03-09"
publishDate: "2026-03-09"
series:
  - Topological K-theory
prerequisites:
  - "/blog/lower-K-theory/lower-K-theory.md"
#  - "/blog/abouttheme.md"
#syndicate:
#  - "https://example.org"
Summary: "Using the projective class group and Wall's finitness obstruction to determine if a space can be homotopy equivalent to a finite CW complex."
audio: []
videos: []
images: []
---

# Introduction

The objective of this post is to decide if a "simple" topological space can be "similar" to a "simple" and "easily describable" one. In more technical terms, we want to determine if a given CW-Complex can be homotopy equivalent to a finite CW complex. This is interesting as finite CW complexes are easier to work with and have nicer properties such as being compact and having finitely generated homology groups. This is a first approximation to the problem of determining if a CW-complex is homotopy equivalent to a compact manifold.

I will ommit the definition of basic concepts in Algebraic Topology such as CW-complexes, homotopy equivalences and fundamental groups. If at some point I make a post on basic algebraic topology I will link it here as a prerequisite.

# Wall's finitness obstruction on chain complexes

We now proceed to define a similar result in chain complexes that will be easily generalized to topological spaces.

## Finite domination of chain complexes

We start introducing notation for chain complexes:

{{< mathdef type="Definition" name="Types of chain complexes" >}}
Let $R$ be a ring. We say a $R$-chain complex $C_*$ is:

<ul>
<li><strong>finitely generated</strong> if each $C_n$ is a finitely generated $R$-module.</li>
<li><strong>projective</strong> if each $C_n$ is a projective $R$-module.</li>
<li><strong>free</strong> if each $C_n$ is a free $R$-module.</li>
<li><strong>positive</strong> if $C_n = 0$ for $n < 0$.</li>
<li><strong>finite dimensional</strong> if $C_n = 0$ for $n > N$ for some $N \in \mathbb{N}$.</li>
<li><strong>finite</strong> if it is finitely generated and finite dimensional.</li>
</ul>

{{< /mathdef >}}

{{< mathdef type="Definition" name="Finite domination in CW-complexes" >}}
Let $R$ be a ring. We say a $R$-chain complex $C_*$ is <strong>finitely dominated</strong> if there exists a finite free $R$-chain complex $D_*$ and chain maps $i_*: C_* \to D_*$ and $r_*: D_* \to C_*$ such that $r_* \circ i_*$ is chain homotopic to the identity on $C_*$.

In this case we say $(D_*, i_*, r_*)$ is a <strong>finite domination</strong> of $C_*$.
{{< /mathdef >}}

Let's start with a simple example of a finitely dominated chain complex that is not finite:

{{< mathdef type="Example" >}}
Consider the $\mathbb{Z}$-chain complex $C_*$ defined as follows:

$$0\xrightarrow{} \bigoplus_{i=1}^{\infty}\mathbb{Z}\xrightarrow{id} \bigoplus_{i=1}^{\infty}\mathbb{Z} \xrightarrow{} 0$$

where $C_0 \cong C_1 \cong \bigoplus_{i=1}^{\infty}\mathbb{Z}$. Notice that this chain complex is finitely dimensional but not finitely generated so it is not finite.
However, it is finitely dominated as we can take $D_*$ to be the 0 chain complex:

$$D_n = 0 \text{ for all } n.$$

We can define $i_*: C_* \to D_*$ and $r_*: D_* \to C_*$ as the zero maps. Then $(D_*, i_*, r_*)$ is a finite domination of $C_*$.

Indeed, it is enough to check that $r_* \circ i_*=0_{C_*}$ is chain homotopic to the identity on $C_*$. That is, we need to find maps $h_n: C_n \to C_{n+1}$ such that

$$d^C_{n} \circ h_n + h_{n-1} \circ d^C_{n-1} = id_{C_n}-0_{C_n} \text{ for all } n.$$

As the only non-zero $C_n$ are $C_0$ and $C_1$, we only need to check the cases $n=0$ and $n=1$. 

If we define $h_0: C_0 \to C_1$ as the identity map and $h_n = 0$ for all $n \neq 0$. Then we have:
$$\begin{align*}
d^C_{0} \circ h_0 + h_{-1} \circ d^C_{-1} = id \circ id + 0 \circ 0 &= id_{C_0} \\
d^C_{1} \circ h_1 + h_{0} \circ d^C_{0} = 0 \circ 0 + id \circ id &= id_{C_1}
\end{align*}$$

{{< /mathdef >}}

## Wall's finitness obstruction for chain complexes

To define the finitness obstruction we need one final result:

{{< mathdef type="Theorem">}}
Let $C$ be a chain-complex. $C$ has a finite domination if and only if $C$ is chain homotopy equivalent to a finite projective chain complex.
{{< /mathdef >}}

Using this theorem we can finally define the finitness obstruction:

{{< mathdef type="Definition" name="Finitness obstruction of a chain complex" >}}
Let $C_*$ be a $R$-chain complex with a finite domination $(D_*, i_*, r_*)$ where $D_*$ is a finite projective $R$-chain complex. We define the <strong>finitness obstruction</strong> $o(C_*)$ as 
$$o(C_*) = \sum_{n} (-1)^n [D_n] \in K_0(R)$$
where $[D_n]$ is the class of the projective module $D_n$ in the projective group $K_0(R)$.
{{< /mathdef >}}

One last, and more relevant, definition remains:

{{< mathdef type="Definition" name="Reduced finiteness obstruction" >}}
Let $C_*$ be a $R$-chain complex with a finite domination $(D_*, i_*, r_*)$ where $D_*$ is a finite projective $R$-chain complex. We define the <strong>reduced finiteness obstruction</strong> $\tilde{o}(C_*)$ as 
$$\tilde{o}(C_*) = \sum_{n} (-1)^n [D_n] \in \tilde{K_0}(R)$$
where $[D_n]$ is the class of the projective module $D_n$ in the reduced projective group $\tilde{K_0}(R)$.
{{< /mathdef >}}

In particular, the reduced finitness obstruction is the image of the finitness obstruction under the natural projection $K_0(R) \to \tilde{K}_0(R)$.

In the previous example we have $o(C_*) = 0$ because $D_n = 0$ for all $n$ (Because $D_*$ is already a finite projective chain complex it can be used for the computation).

## Examples and computations

It is in general very hard to compute the finitness obstruction of a chain complex. However, if we find that the projective group $K_0(R)$ is trivial, then we can conclude that the finitness obstruction of any $R$-chain complex is trivial. Equivalently, if the reduced projective group $\tilde{K}_0(R)$ is trivial, then the reduced finitness obstruction of any $R$-chain complex is also trivial.

{{< mathdef type="Example" >}}
Let $C_*$ be a $\mathbb{Z}[\mathbb{Z}/2]$-chain complex with a finite domination. As $K_0(\mathbb{Z}[\mathbb{Z}/2]) \cong \mathbb{Z}$, we have that $o(C_*) = [\mathbb{Z}^n]$ for some $n \in \mathbb{Z}$. However, as $\tilde{K}_0(\mathbb{Z}[\mathbb{Z}/2]) = 0$, we have that $\tilde{o}(C_*) = 0$.
{{< /mathdef >}}

It can be usefull to have more powerfull results to calculate the finitness obstruction.

{{< mathdef type="Lemma">}}
<ol>
<li>
If a $R$-chain complex $C_*$ is chain homotopy equivalent to a finitely dominated $R$-chain complex $D_*$, then $C_*$ is finitely dominated and 
$$o(C_*) = o(D_*).$$
That is, the finitness obstruction is a homotopy invariant.
</li>
<li> Let $0 \to C_* \to D_* \to E_* \to 0$ be a short exact sequence of $R$-chain complexes. If two of the chain complexes are finitely dominated, then the third one is also finitely dominated and
$$o(D_*) = o(C_*) + o(E_*).$$
That is, the finitness obstruction is additive on short exact sequences.
</li>
<li> Let $C_*$ be a finitely dominated $R$-chain complex, then $\tilde{o}(C_*) = 0$ if and only if $C_*$ is chain homotopy equivalent to a finite free $R$-chain complex.
</ol>
{{< /mathdef >}}

This theorem hints at the idea that the finitness obstruction defines a surjection between the homotopy classes of finitely dominated $R$-chain complexes and the isomorphism classes of finitely generated projective modules. This result is not hard to prove. More so Wall's finitness obstruction proves something similar for spaces.

> [!NOTE]
> I need to add an example of usage of this to find the finitness obstruction of a chain complex that is not 0, but I haven't been able to make tikcd work here yet so I will deal with it later.

# Wall's finitness obstruction for topological spaces

With the prerequisites out of the way, we can now define the finitness obstruction for topological spaces. The idea is to use the cellular chain complex of a CW-complex to define the finitness obstruction of the space.

## Finite domination of topological spaces

We start by defining some basic concepts over CW-complexes:

{{< mathdef type="Definition" name="Finite domination in CW-complexes" >}}
A CW-complex $X$ is <strong>finitely dominated</strong> if there exists a finite CW-complex $Y$ and maps $i: X \to Y$ and $r: Y \to X$ such that $r \circ i$ is homotopic to the identity on $X$.

In this case we say $(Y, i, r)$ is a <strong>finite domination</strong> of $X$.
{{< /mathdef >}}

The objective of this post is to find out when the other direction in $i$ and $r$ could be possible, if $X$ is finitelly dominated by $(Y, i, r)$ then it only needs for $i\circ r$ to be homotopy equivalent to the identity in $Y$ for $X$ and $Y$ to be homotopy equivalent.

We can see now an example of a finitely dominated space that is not homotopy equivalent to a finite CW-complex:

{{< mathdef type="Example" >}}
Consider the infinite-dimensional sphere $S^{\infty} = \bigcup_{n=0}^{\infty} S^n$. This space is not homotopy equivalent to a finite CW-complex as it has infinitely many non-trivial homology groups. However, it is finitely dominated because it is contractible. We can take $Y = \{*\}$ to be a single point. We can define $i: S^{\infty} \to \{*\}$ as the constant map and $r: \{*\} \to S^{\infty}$ as the inclusion of the base point. Then $(\{*\}, i, r)$ is a finite domination of $S^{\infty}$.
{{< /mathdef >}}

## Finiteness obstruction of topological spaces

We want to define the finitness obstruction of a topological space $X$ using the cellular chain complex of a CW-complex that is homotopy equivalent to $X$. 

One naive approach to define such an obstruction would be to calculate it over $C_\*(X)$. However we are interested in the homotopic properties of $X$ so we would like to work over a $\mathbb{Z}\pi_1(X)$-chain complex (while $C_\*(X)$ is just a $\mathbb{Z}$-chain complex). To achieve this we resort to $\tilde{X}$, the universal covering of $X$, whose cellular chain complex $C_*(\tilde{X})$ is a $\mathbb{Z}\pi_1(X)$-chain complex because $\pi_1(X)$ acts on $\tilde{X}$ by deck transformations.

> [!NOTE]
> I would like to at some point go into more depth as to why we are using the covering space instead of the original.

Knowing $X$ is finitely dominated it is posible to build a finite domination for $C_*(\tilde{X})$ using the finite domination of $X$:

Let $(Y, i, r)$ be a finite domination of $X$. We can build a covering $\overline{Y}$ of $Y$, such that $\pi_1(\overline{Y}) \cong \pi_1(X)$. This can be done because $r_*: \pi_1(Y) \to \pi_1(X)$ is a group epimorphism so $\pi_1(X) \leq \pi_1(Y)$.

We then bring that covering back to $X$ by taking the pullback of $\overline{Y}$ along $i: X \to Y$ which gives us the covering $i^*\overline{Y}= \{(x, y) \in X \times \overline{Y} : i(x) = p(y)\}$ (Essentially the fiber product $X \times_Y \overline{Y}$). 

The maps $i: X \to Y$ and $r: Y \to X$ can be lifted to $\mathbb{Z}\pi_1(X)$-chain maps $i_\*: C_\*(\tilde{X}) \to C_\*(\overline{Y})$ and $r_\*: C_\*(\overline{Y}) \to C_\*(\tilde{X})$ respectively because the pullback $i^\*\overline{Y}$ is a covering of $X$ and $\tilde{X}$ is the universal covering of $X$, so there exists a unique lift of $i$ and $r$ to maps between the coverings. In particular $r_* \circ i_\*$ is chain homotopic to the identity on $C_\*(\tilde{X})$ and $(C_\*(i^\*\overline{Y}), i_\*, r_\*)$ is a finite domination of $C_*(\tilde{X})$.

We can now define the finitness obstruction of $X$

{{< mathdef type="Definition" name="Unreduced finiteness obstruction of a topological space" >}}
Let $X$ be a finitely dominated connected CW-complex. We define the <strong>unreduced finiteness obstruction</strong> $o(X)$ as
$$o(X) = o(C_*(\tilde{X})) \in K_0(\mathbb{Z}\pi_1(X))$$
where $o(C_*(\tilde{X}))$ is the finitness obstruction of the $\mathbb{Z}\pi_1(X)$-chain complex $C_*(\tilde{X})$.
{{< /mathdef >}}

And similarly for the reduced finitness obstruction:

{{< mathdef type="Definition" name="Finiteness obstruction of a topological space" >}}
Let $X$ be a finitely dominated connected CW-complex. We define the <strong>finiteness obstruction</strong> $\tilde{o}(X)$ as
$$\tilde{o}(X) = \tilde{o}(C_*(\tilde{X})) \in \tilde{K}_0(\mathbb{Z}\pi_1(X))$$
where $\tilde{o}(C_*(\tilde{X}))$ is the reduced finitness obstruction of the $\mathbb{Z}\pi_1(X)$-chain complex $C_*(\tilde{X})$.
{{< /mathdef >}}

The conectedness condition follows from the definition of the fundamental group, but it can be circunvented by defining 
$$K_0(\mathbb{Z}\pi_1(X)) = \bigoplus_{C\in \pi_0(X)} K_0(\mathbb{Z}\pi_1(C))$$
and similarly for the reduced projective group.

In this case the obstructions are defined as
$$o(X) = \bigoplus_{C\in \pi_0(X)} o(C) \in K_0(\mathbb{Z}\pi_1(X))$$
$$\tilde{o}(X) = \bigoplus_{C\in \pi_0(X)} \tilde{o}(C) \in \tilde{K}_0(\mathbb{Z}\pi_1(X))$$

The power of the finitness obstruction is that it gives us a way to determine if a space can be homotopy equivalent to a finite CW-complex:

{{< mathdef type="Theorem" name="Wall's finitness obstruction for topological spaces" >}}
Let $X$ be a finitely dominated connected CW-complex. 
<ol>
<li> $X$ is homotopy equivalent to a finite CW-complex if and only if $\tilde{o}(X) = 0$. </li>
<li> If a group $G$ is finitely presented, then every element of $K_0(\mathbb{Z}G)$ can be realized as the finitness obstruction of some finitely dominated 3-dimensional CW-complex with fundamental group $G$. </li>
</ol>
{{< /mathdef >}}

The first part of the theorem is the main result in this post and explains our interest in exploring the projective groups of topological spaces. 

The second part of the theorem is a realization result that shows that the finitness obstruction gives as a surjective inclusion of topological spaces with fundamental group $G$ into the projective group $K_0(\mathbb{Z}G)$ and its reduced version $\tilde{K}_0(\mathbb{Z}G)$ by projecting.

## Examples and computations

Obtaining the finitness obstruction of a chain complex is usually not a simple computation, obtaining it from a topological space doesn't make it easier. In this case the easiest way to apply Wall's finitness obstruction is to use that the reduced projective group of the group ring of its fundamental class is trivial even if it's only a sufficient condition.

{{< mathdef type="Example">}}
  Consider again $S^\infty$, we know its fundamental group is $\pi_1(S^\infty)=0$ because it is contractible so $K_0(\mathbb{Z}\pi_1(S^\infty))=K_0(\mathbb{Z})$ and we know $\tilde{K}_0(\mathbb{Z})=0$ so the finitness obstruction is zero which implies $S^\infty$ is homotopy equivalent to a point.
{{< /mathdef >}}

There are also finitely dominated spaces that are not homotopy equivalent to a finite CW-complex

{{< mathdef type="Example">}}
Consider the group $\mathbb{Z}/12$. By the 
<a href="/blog/lower-k-theory/lower-k-theory/#tildeK0FiniteAbelian" > Finite abelian groups with vanishing $\tilde{K_0}(\mathbb{Z}G)$ theorem </a> 
we know $\tilde{K_0}(\mathbb{Z}[\mathbb{Z}/12])\neq 0$ and, by Wall's finitness obstruction, for any $e\neq 0\in \tilde{K_0}(\mathbb{Z}[\mathbb{Z}/12])$ there exists a finitely dominated topological space $X$ with fundamental group $\mathbb{Z}/12$ such that $\tilde{o}(X)=e\neq 0$ which implies $X$ is not homotopically equivalent to a finite CW-complex.
{{< /mathdef >}}
<!--![image](/blog/page_001.webp)-->

