# Seminar-Style Exemplars

## Exemplar 1: Mixed-Audience Hook

**Scenario:** Department seminar  
**Domain:** Applied Mathematics  
**Audience:** Mixed math faculty, grad students, and a few visitors from engineering  
**Input material type:** Opening motivation slide

### Slide content summary
- Title: "Sparse recovery under non-convex constraints"
- Bullets:
  - Classical compressed sensing assumes convexity
  - Many real-world constraints are non-convex
  - Need new theoretical guarantees

### Weak script
"Classical compressed sensing assumes convexity. Many real-world constraints are non-convex. We need new theoretical guarantees."

### Critique
- Starts with jargon (compressed sensing, convexity) without a hook.
- A visitor from engineering may not know what compressed sensing is.
- No stakes: why does non-convexity matter?
- No narrative thread.

### Improved script
"Imagine you are trying to reconstruct an image from a small number of measurements — like a medical scan where you want to minimize radiation exposure. The standard theory tells you this is possible if the problem is convex, which basically means the solution landscape is smooth and predictable. But in many real applications — like MRI with physical hardware constraints or network inference with discrete topology — the problem is not convex. It has holes, ridges, and multiple local minima. The question is: can you still guarantee a correct recovery? The classical answer is no. Our answer is: yes, under conditions we can characterize."

### Why the revision works
- Opens with a concrete scenario (medical scan, radiation) that everyone understands.
- Defines convexity intuitively before using the term.
- Explains why non-convexity is hard (holes, ridges, local minima).
- Frames the contribution as resolving a clear tension.

---

## Exemplar 2: Intuition-Before-Detail Transition

**Scenario:** Department seminar  
**Domain:** Physics  
**Audience:** Mixed physics faculty and grad students  
**Input material type:** Methods slide with equation

### Slide content summary
- Title: "Renormalization group flow"
- Equation: beta(g) = -epsilon g + g^3
- No intuitive explanation on slide

### Weak script
"The renormalization group flow is governed by the beta function: beta of g equals minus epsilon g plus g cubed. This describes how the coupling constant changes with scale."

### Critique
- Reads the equation without explaining what it means physically.
- A subset of the audience may know RG flow, but the equation is meaningless without intuition.
- No connection to the physical phenomenon.

### Improved script
"The key idea of the renormalization group is that physics looks different at different scales. If you zoom out far enough, the microscopic details blur away and only a few parameters matter. The beta function tells you how those parameters change as you zoom out. In our case, the coupling constant g starts large at short distances, but as you zoom out, the first term pulls it down while the cubic term pushes it back up. The balance between those two forces determines whether the system flows to a fixed point or keeps changing forever. So this simple equation — minus epsilon g plus g cubed — encodes the entire long-distance behavior of the theory."

### Why the revision works
- Explains the physical meaning of RG flow before showing the equation.
- Uses the zoom metaphor to make scale invariance intuitive.
- Describes the two competing terms in the equation as physical forces.
- Gives the audience a reason to care about the equation before reading it.
