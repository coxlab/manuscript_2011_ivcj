<%def name="p(perf_tuple)">${"%.1f" % perf_tuple[0]} $\pm$ ${"%.1f" % perf_tuple[1]}</%def>
<%def name="plb(perf_tuple)">${"%.1f" % perf_tuple[0]} $\pm$ ${"%.1f" % perf_tuple[1]} </%def>

\begin{table}
\begin{center}
\caption{Performance (\emph{LFW} Restricted View 2) of the family of biologically-inspired models and blends thereof.}

\centering
\scalebox{0.9}{%

\begin{tabular*}{1\textwidth}{ l | c | c | c | c || c |}

## =============================================================================
\cline{2-6}
& \hspace{.5cm} alone \hspace{.5cm}
& \hspace{.5cm} $+$crops \hspace{.5cm} 
& within blend
& \emph{V1}$+$\emph{L2}$+$\emph{L3}
& \emph{V1}$+$\emph{L2}$+$\emph{L3}$_{(weighted)}
$${"\\\\"} 

## =============================================================================
\cline{1-6}
\multicolumn{1}{|l|}{{\bf\emph{V1-like}}}
& ${p(v1like_a_plus)}
& ${p(v1like_a_plus_crops)} 
& 
& \multirow{13}{*}{ \bf{${plb(v1_l2_l3_blend)}} } 
& \multirow{13}{*}{ \bf{${plb(v1_l2_l3_weighted_blend)}} } 
${"\\\\"}

## =============================================================================
\cline{1-4}
\multicolumn{4}{|l|}{{\bf\emph{HT-L2}}} & & ${"\\\\"} 
\cline{1-4}
##\cline{6-6}

## -----------------------------------------------------------------------------
\multicolumn{1}{|l|}{5th} 
& ${p(ht_l2_5th)}
& ${p(ht_l2_5th_crops)} 
& \multirow{5}{*}{ ${plb(l2_l3_blend)} } 
& & ${"\\\\"}

## -----------------------------------------------------------------------------
\multicolumn{1}{|l|}{4th}
& ${p(ht_l2_4th)}
& ${p(ht_l2_4th_crops)}
& & & ${"\\\\"} 

## -----------------------------------------------------------------------------
\multicolumn{1}{|l|}{3rd}
& ${p(ht_l2_3rd)}
& ${p(ht_l2_3rd_crops)}
& & & ${"\\\\"} 

## -----------------------------------------------------------------------------
\multicolumn{1}{|l|}{2nd}
& ${p(ht_l2_2nd)}
& ${p(ht_l2_2nd_crops)} 
& & & ${"\\\\"} 

## -----------------------------------------------------------------------------
\multicolumn{1}{|l|}{1st}
& ${p(ht_l2_1st)} 
& ${p(ht_l2_1st_crops)}
& & & ${"\\\\"} 

## =============================================================================
\cline{1-4}
\multicolumn{4}{|l|}{{\bf\emph{HT-L3}}} & & ${"\\\\"} 
\cline{1-4}

## -----------------------------------------------------------------------------
\multicolumn{1}{|l|}{5th}
& ${p(ht_l3_5th)}
& ${p(ht_l3_5th_crops)} 
& \multirow{5}{*}{ ${plb(ht_l3_blend)} } 
& & ${"\\\\"}

## -----------------------------------------------------------------------------
\multicolumn{1}{|l|}{4th}
& ${p(ht_l3_4th)}
& ${p(ht_l3_4th_crops)}
& & & ${"\\\\"} 

## -----------------------------------------------------------------------------
\multicolumn{1}{|l|}{3rd}
& ${p(ht_l3_3rd)}
& ${p(ht_l3_3rd_crops)} 
& & & ${"\\\\"} 

## -----------------------------------------------------------------------------
\multicolumn{1}{|l|}{2nd}
& ${p(ht_l3_2nd)}
& ${p(ht_l3_2nd_crops)} 
& & & ${"\\\\"} 

## -----------------------------------------------------------------------------
\multicolumn{1}{|l|}{1st}
& ${p(ht_l3_1st)} 
& ${p(ht_l3_1st_crops)}  
& & & ${"\\\\"} 

\cline{1-6}

\end{tabular*}
}
\label{tab:grand_performance_table}
\end{center}
\end{table}


