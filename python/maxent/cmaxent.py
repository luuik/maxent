# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.




"""
maxent - Python binding for C++ Conditional Maximum Entropy Model.

"""


from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_cmaxent', [dirname(__file__)])
        except ImportError:
            import _cmaxent
            return _cmaxent
        if fp is not None:
            try:
                _mod = imp.load_module('_cmaxent', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _cmaxent = swig_import_helper()
    del swig_import_helper
else:
    import _cmaxent
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class MaxentModel(_object):
    """Proxy of C++ maxent::MaxentModel class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MaxentModel, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MaxentModel, name)
    __repr__ = _swig_repr
    def __init__(self): 
        """
        __init__(self) -> MaxentModel

        Create an empty MaxentModel instance
        """
        this = _cmaxent.new_MaxentModel()
        try: self.this.append(this)
        except: self.this = this
    def __str__(self):
        """
        __str__(self) -> char *

        Create an empty MaxentModel instance
        """
        return _cmaxent.MaxentModel___str__(self)

    def load(self, *args):
        """
        load(self, model)

        Load a MaxentModel from a file
        """
        return _cmaxent.MaxentModel_load(self, *args)

    def save(self, *args):
        """
        save(self, model, binary=False)
        save(self, model)

        Save current model to a file. 
        Parameters: 
        model   The filename of the model to save.  
        binary  If true, the file is saved in binary format, which is
        usually smaller (if compiled with libz) and much faster to
        load.
        """
        return _cmaxent.MaxentModel_save(self, *args)

    def eval(self, *args):
        """
        eval(self, context, outcome) -> double

        This method calculates the conditional probability p(y|x) for given x
        (context) and y (outcome).

        Parameters: 
        context  A list of pair (string,  float) indicates names of the contextual
        predicates and their values which are to be evaluated together.  
        outcome  The outcome label for which the conditional probability is
        calculated.  

        If only string context is given, their values are assumed to be 1.0

        Returns: 
        The conditional probability of p(outcome|context).
        """
        return _cmaxent.MaxentModel_eval(self, *args)

    def predict(self, *args):
        """
        predict(self, context) -> maxent::MaxentModel::outcome_type

        Evaluates a context,  return the most possible outcome y for given context x.
        """
        return _cmaxent.MaxentModel_predict(self, *args)

    def begin_add_event(self):
        """
        begin_add_event(self)

        Signal the begining of adding event (the start of training). 

        This method must be called before adding any event to the model. It informs
        the model the beginning of training. 

        After the last event is added end_add_event() must be called to indicate the
        ending of adding events.
        """
        return _cmaxent.MaxentModel_begin_add_event(self)

    def add_event(self, *args):
        """
        add_event(self, context, outcome, count=1)

        Add an event (context, outcome, count) to current model for training later. 

        add_event() should be called after calling begin_add_event(). 

        Parameters: 
        context  A list of pair (string, float) to indicate the context
        predicates and their values (must be >= 0) occured in the event. Feature value
        is assumed to be 1.0 if omitted.
        outcome  A string indicates the outcome label.  
        count  How many times this event occurs in training set. default = 1
        """
        return _cmaxent.MaxentModel_add_event(self, *args)

    def add_heldout_event(self, *args):
        """
        add_heldout_event(self, context, outcome, count=1)
        add_heldout_event(self, context, outcome)

        Add an event (context, outcome, count) to current model for training later. 

        add_event() should be called after calling begin_add_event(). 

        Parameters: 
        context  A list of pair (string, float) to indicate the context
        predicates and their values (must be >= 0) occured in the event. Feature value
        is assumed to be 1.0 if omitted.
        outcome  A string indicates the outcome label.  
        count  How many times this event occurs in training set. default = 1
        """
        return _cmaxent.MaxentModel_add_heldout_event(self, *args)

    def end_add_event(self, cutoff=1):
        """
        end_add_event(self, cutoff=1)
        end_add_event(self)

        Signal the ending of adding events. 

        This method must be called after adding of the last event to inform the model
        the ending of the adding events.

        Parameters: 
        cutoff  Event cutoff,  all events that occurs less than cutoff times will be
        discussed. Default = 1 (remain all events). Please note this is different from
        the usual sense of *feature cutoff*.
        """
        return _cmaxent.MaxentModel_end_add_event(self, cutoff)

    def train(self, iter=15, method="lbfgs", sigma2=0.0, tol=1E-05):
        """
        train(self, iter=15, method="lbfgs", sigma2=0.0, tol=1E-05)
        train(self, iter=15, method="lbfgs", sigma2=0.0)
        train(self, iter=15, method="lbfgs")
        train(self, iter=15)
        train(self)

        Train a ME model using selected training method. 

        Parameters: 
        iter  Specify how many iterations are need for iterative methods. Default
        is 15 iterations. 
        method  The training method to use. Can be 'lbfgs' or 'gis'. L-BFGS is used
        as the default training method. 
        sigma2  Global variance (sigma^2) in Gaussian prior smoothing. Default is 0,  which
        turns off Gaussian smoothing. 
        tol  Tolerance for detecting model convergence. Read manual for details.

        """
        return _cmaxent.MaxentModel_train(self, iter, method, sigma2, tol)

    def eval_all(self, *args):
        """
        eval_all(self, context) -> std::vector< pair< maxent::MaxentModel::outcome_type,double > >

        Evaluates a context, return the conditional distribution of given context
        as a list of (outcome, probability) pairs. 

        This method calculates the conditional probability p(y|x) for each possible
        outcome tag y. 

        Parameters: 
        context  A list of string names of the contextual predicates which are to
        be evaluated together. Feature values are assumed to be 1.0 if omitted.

        """
        return _cmaxent.MaxentModel_eval_all(self, *args)

    def is_feature_in_model(self, *args):
        """
        is_feature_in_model(self, feature) -> bool

        Evaluates whether a feature belongs to the model.

        Parameters: 
        feature  one instance of feature

        """
        return _cmaxent.MaxentModel_is_feature_in_model(self, *args)

    def is_outcome_in_model(self, *args):
        """
        is_outcome_in_model(self, outcome) -> bool

        Evaluates whether an outcome belongs to the model.

        Parameters: 
        outcome  one instance of outcome

        """
        return _cmaxent.MaxentModel_is_outcome_in_model(self, *args)

    __swig_destroy__ = _cmaxent.delete_MaxentModel
    __del__ = lambda self : None;
MaxentModel_swigregister = _cmaxent.MaxentModel_swigregister
MaxentModel_swigregister(MaxentModel)
cvar = _cmaxent.cvar

# This file is compatible with both classic and new-style classes.


